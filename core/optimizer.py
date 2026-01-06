# optimizer.py
# File per l'analisi e il calcolo del portfolio ideale

from scipy.optimize import minimize
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

class Optimizer:

    # Funzione per calcolare statistiche sui primi N mesi
    @staticmethod
    def first_months(daily_pct_change, daily_close_px, end_date, first_n_months):
        first_months = daily_pct_change.loc[:end_date]
        first_months = first_months.iloc[:first_n_months * 21] # In caso passare 21 come parametro, per rifinitura più pro

        # Calcola la matrice di covarianza
        cov_matrix = first_months.cov()

        monthly_returns = daily_close_px
        monthly_returns = monthly_returns.resample('ME').last().pct_change().dropna()

        return monthly_returns, cov_matrix

    # # Funzioni per il calcolo del portfolio tramite metodo analitico

    # Funzione per calcolare il rendimento atteso del portafoglio
    @staticmethod
    def portfolio_return(weights, expected_returns):
        return np.sum(weights * expected_returns)

    @staticmethod
    def portfolio_risk(weights, cov_matrix):
        return np.sqrt(np.dot(weights.T, np.dot(cov_matrix, weights)))

    # Funzione per calcolare la varianza del portafoglio
    @staticmethod
    def portfolio_variance(weights, cov_matrix):
        return np.dot(weights.T, np.dot(cov_matrix, weights))

    # Funzione per calcolare lo Sharpe ratio
    @staticmethod
    def negative_sharpe_ratio(weights, expected_returns, cov_matrix, risk_free_rate=0):
        port_return = Optimizer.portfolio_return(weights, expected_returns)
        port_volatility = np.sqrt(Optimizer.portfolio_variance(weights, cov_matrix))
        return - (port_return - risk_free_rate) / port_volatility

    # Funzione di vincolo (i pesi devono sommare a 1)
    @staticmethod
    def check_sum(weights):
        return np.sum(weights) - 1

    # Funzione per il calcolo dei rendimenti attesi
    @staticmethod
    def optimal_weights(monthly_returns, tickers, expected_returns):
        np.set_printoptions(suppress=True)

        # Dati dei rendimenti passati e attesi
        expected_returns_past = monthly_returns.mean().clip(-0.02, 0.02)
        cov_matrix_past = monthly_returns.cov()
        expected_returns_future = np.array(
            [expected_returns[t] for t in tickers],
            dtype=float
        )

        if expected_returns_future.shape[0] != len(tickers):
            raise ValueError("Expected returns length mismatch")



        # Verifica che la lunghezza corrisponda ai tickers
        if len(expected_returns_future) != len(tickers):
            raise ValueError(
                f"Dimensione rendimenti ({len(expected_returns_future)}) non coincide con numero tickers ({len(tickers)})")

        # Metodo analitico con rendimenti passati
        initial_guess = np.ones(len(tickers)) / len(tickers)
        constraints = ({'type': 'eq', 'fun': Optimizer.check_sum})
        
        if len(tickers) > 3:
            bounds = tuple((0.01, 0.25) for _ in range(len(tickers)))
        else:
            bounds = tuple((0.01, 1) for _ in range(len(tickers)))

        opt_results_past = minimize(Optimizer.negative_sharpe_ratio, initial_guess, args=(expected_returns_past, cov_matrix_past),
                                    method='SLSQP', bounds=bounds, constraints=constraints)

        # Metodo analitico con rendimenti attesi
        opt_results_future = minimize(Optimizer.negative_sharpe_ratio, initial_guess,
                                      args=(expected_returns_future, cov_matrix_past),
                                      method='SLSQP', bounds=bounds, constraints=constraints)

        optimal_weights_past_analytical = opt_results_past.x
        optimal_weights_future_analytical = opt_results_future.x

        return optimal_weights_past_analytical, optimal_weights_future_analytical, expected_returns_past, cov_matrix_past

    # Funzione per la simulazione di MonteCarlo
    @staticmethod
    def montecarlo_sim(prezzi, n_giorni, num_portfolios, dati_mercato, tickers, expected_returns_past,
                       cov_matrix_past, optimal_weights_past_analytical, optimal_weights_future_analytical):
        plt.rcParams['figure.figsize'] = [10, 6]
        plt.rcParams['figure.dpi'] = 300

        ritorni_semplici = prezzi.pct_change().dropna()
        ritorni_medi = ritorni_semplici.mean() * n_giorni
        mat_cov = ritorni_semplici.cov() * n_giorni

        # Funzione per calcolare il rendimento e la varianza del portafoglio
        def performance_portafoglio(pesi, rendimenti, matrice_cov):
            rendimento_portafoglio = np.sum(rendimenti * pesi)
            varianza_portafoglio = np.dot(pesi.T, np.dot(matrice_cov, pesi))
            return rendimento_portafoglio, varianza_portafoglio

        ritorni_mercato = dati_mercato.pct_change().dropna()

        # Assicurati che i ritorni di mercato siano allineati con ritorni_semplici
        ritorni_semplici = ritorni_semplici.loc[ritorni_mercato.index]

        # Funzione per calcolare il beta del portafoglio
        def calcola_beta(rendimenti_portafoglio, rendimenti_mercato):
            covarianza = np.cov(rendimenti_portafoglio, rendimenti_mercato)[0, 1]
            varianza_mercato = np.var(rendimenti_mercato)
            beta = covarianza / varianza_mercato
            return beta

        # Calcolo dei rendimenti del portafoglio con pesi ottimali trovati dalla simulazione Monte Carlo
        def calcola_rendimenti_portafoglio(pesi, rendimenti_asset):
            rendimenti_portafoglio = np.dot(rendimenti_asset, pesi)
            return rendimenti_portafoglio

        # Simulazione Monte Carlo con rendimenti passati
        results_past = np.zeros((3, num_portfolios))
        weights_record_past = []

        for i in range(num_portfolios):
            weights = np.random.random(len(tickers))
            weights /= np.sum(weights)
            weights_record_past.append(weights)

            port_return_past = Optimizer.portfolio_return(weights, expected_returns_past)
            port_risk_past = np.sqrt(Optimizer.portfolio_variance(weights, cov_matrix_past))

            results_past[0, i] = port_return_past
            results_past[1, i] = port_risk_past
            results_past[2, i] = port_return_past / port_risk_past

        # Trova l'indice del portafoglio con il miglior Sharpe ratio
        max_sharpe_idx_past = np.argmax(results_past[2])
        max_sharpe_port_past = results_past[:, max_sharpe_idx_past]

        # Plotting
        plt.figure(figsize=(12, 8))
        plt.scatter(results_past[1, :], results_past[0, :], c=results_past[2, :], cmap='viridis', marker='o', s=10,
                    alpha=0.3)

        # Evidenzia i portafogli ottimali
        plt.scatter(np.sqrt(Optimizer.portfolio_variance(optimal_weights_past_analytical, cov_matrix_past)),
                    Optimizer.portfolio_return(optimal_weights_past_analytical, expected_returns_past) * 12, color='red',
                    marker='*', s=500, label='Analytical - Past Returns')

        plt.scatter(np.sqrt(Optimizer.portfolio_variance(optimal_weights_future_analytical, cov_matrix_past)),
                    Optimizer.portfolio_return(optimal_weights_future_analytical, expected_returns_past) * 12, color='orange',
                    marker='*', s=500, label='Analytical - Future Returns')

        plt.scatter(max_sharpe_port_past[1], max_sharpe_port_past[0], color='green', marker='D', s=200,
                    label='Simulated - Past Returns')

        plt.title('Portafogli Simulati e Ottimali')
        plt.xlabel('Rischio (Deviazione Standard)')
        plt.ylabel('Rendimento Atteso')
        plt.colorbar(label='Sharpe Ratio')
        plt.legend()
        plt.grid(True)
        plt.show()

    @staticmethod
    def best_weights(tickers, optimal_weights_future_analytical):

        data = {"Ticker": tickers,
                "% Pesi": optimal_weights_future_analytical * 100
        }

        pesi_migliori = pd.DataFrame(data)
        return pesi_migliori