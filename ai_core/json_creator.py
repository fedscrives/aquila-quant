# json_creator.py
# File per la creazione dei Json da dare come input agli LLM

import numpy as np

class JsonCreator:

    # Funzione per la creazione del json dei primi dati scaricati
    @staticmethod
    def data_json(all_data_tail, rend_com, cum_daily_return, tickers, years):

        cagr = (cum_daily_return.iloc[-1])**(1/years) - 1


        data_json = {"latest_datas": {
            "description": "Ultimi valori di chiusura disponibili per ciascun titolo",
            "ticker_order": tickers,
            "values": all_data_tail
        },
            "compound_returns": {
                "description": "Rendimenti composti calcolati sull'intero periodo",
                "ticker_order": tickers,
                "values": rend_com
            },
            "cumulative_return_last": {
                "description": "Rendimento cumulato",
                "ticker_order": tickers,
                "years": years,
                "values": cagr
            }
        }

        return data_json

    # Funzione per la creazione del json delle statistiche
    @staticmethod
    def analytics_json(statistics, corr_matrix, cov_matrix, tickers):
        analytics_json = {"descriptive_statistics": {
            "description": "Statistiche descrittive sui rendimenti dei titoli",
            "frequency" : "daily",
            "window" : 252,
            "ticker_order": tickers,
            "metrics": statistics
        },
            "correlation_matrix": {
                "description": "Matrice di correlazione tra i titoli",
                "ticker_order": tickers,
                "values": corr_matrix
            },
            "covariance_matrix": {
                "description": "Matrice di covarianza tra i titoli",
                "ticker_order": tickers,
                "values": cov_matrix
            }
        }

        return analytics_json

    # Funzione per la creazione del json delle strategie
    @staticmethod
    def signal_json(sma, ewm, sma_low, sma_high, ewm_low, ewm_high):
        signal_json = {"medie_mobili_semplici": {
            "description": "Medie mobili semplici per titolo calcolate sull'intero periodo",
            "faster_window": sma_low,
            "slow_window": sma_high,
            "metrics": sma
        },
            "medie_mobili_esponenziali": {
                "description": "Medie mobili esponenziali per titolo calcolate sull'intero periodo",
                "faster_window": ewm_low,
                "slow_window": ewm_high,
                "values": ewm
            }
        }

        return signal_json

    # Funzione per la creazione del json del portfolio
    @staticmethod
    def optimizer_json(risk_free, betas, rit_port_best, pesi_migliori, var_port_best, tickers, sharpe):

        optimizer_json = {"risk_free": {
            "description": "Indice della Banca della Riserva Federale di Saint Louis (FRED), valore mensile",
            "metrics": risk_free
            },
            "betas": {
                "description": "Beta calcolato per ogni titolo",
                "ticker_order": tickers,
                "values": betas
            },
            "portfolio_returns": {
                "description": "Ritorno atteso del portfolio ottimale, mensilmente",
                "values": rit_port_best
            },
            "portfolio_weights": {
                "description": "Pesi dei titoli per il portfolio ottimale",
                "ticker_order": tickers,
                "values": pesi_migliori
            },
            "portfolio_variance": {
                "description": "Varianza attesa per il portfolio ottimale",
                "values": var_port_best
            },
            "sharpe_ratio": {
                "description": "Rendimento del portfolio rispetto ai rischi, calcolato con ritorni e volatilità mensili",
                "values": sharpe
            }
        }

        return optimizer_json