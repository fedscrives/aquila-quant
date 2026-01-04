# analytics.py
# File per calcolare le statistiche dei titoli

import pandas as pd
import numpy as np

class Analytics:
    # Funzione per il calcolo del rendimento composto
    @staticmethod
    def comp_ret(close_px):
        years = (close_px.index[-1] - close_px.index[0]).days / 365.25
        return (close_px.iloc[-1] / close_px.iloc[0]) ** (1 / years) - 1
    
    # Pulizia del rendimento composto
    @staticmethod
    def clean_com_ret(years, daily_close):
        rend_com = Analytics.comp_ret(years, daily_close)
        rend_com_pulito = rend_com.round(4)

        rend_com_pulito['RC_%'] = (rend_com_pulito['RC'] * 100).map('{:.2f}%'.format)
        # Scrivo il ritorno così in modo che si possa prendere tutta la tabella o solo la stampa (mettere _ su quello non richiesto)
        # _, string_comp = '' oppure comp_clean, _ = ''
        return rend_com_pulito, rend_com_pulito[['Ticker', 'Inizio', 'Fine', 'RC_%']].to_string(index=False)
    
    # Funzione per ottenere le chiusure con i cambiamenti percentuali
    @staticmethod
    def pct_change(daily_close):
        daily_pct_change = daily_close.pct_change()
        daily_pct_change.dropna(inplace=True)

        return daily_pct_change
    
    # Funzione per il calcolo del rendimento cumulato
    @staticmethod
    def cum_ret(daily_pct_change):
        #Rendimento cumulato
        cum_daily_return = (1 + daily_pct_change).cumprod()
        # Come sopra, o ritorno tutto o l'ultima riga
        return cum_daily_return, cum_daily_return.tail(1)
    
    # Funzione per il calcolo dei rendimenti lordi e netti
    @staticmethod
    def returns(all_data):
        # 1. CALCOLO RENDIMENTO SEMPLICE LORDO
        # Usiamo groupby per isolare ogni azione: il primo giorno di ogni azione diventerà NaN (corretto)
        # Usiamo parentesi singole per lavorare con i numeri e non con le tabelle
        all_data['RS_Lordo'] = all_data['Close'] / all_data.groupby('Ticker')['Close'].shift(1)
        all_data['RS_Lordo'] = all_data['RS_Lordo'].fillna(1)

        # 2. CALCOLO RENDIMENTO SEMPLICE NETTO
        # La funzione pct_change() fa già (Prezzo_oggi / Prezzo_ieri) - 1
        all_data['RS_Netto'] = all_data.groupby('Ticker')['Close'].pct_change().fillna(0)

        # 3. CALCOLO RENDIMENTO LOGARITMICO
        all_data['RL'] = np.log(all_data['Close'] / all_data.groupby('Ticker')['Close'].shift(1))
        all_data['RL'] = all_data['RL'].fillna(0)

        # --- CREAZIONE DELLE TABELLE PIVOT ---
        # Questo trasforma i dati dal formato "verticale" (all_data) a quello "orizzontale" (tabella per ticker)
        rs_lordo = all_data.pivot_table(values='RS_Lordo', index='Date', columns='Ticker')
        rs_netto = all_data.pivot_table(values='RS_Netto', index='Date', columns='Ticker')
        rl       = all_data.pivot_table(values='RL', index='Date', columns='Ticker')

        return rs_lordo, rs_netto, rl
    
    # Funzione per calcolare la media
    @staticmethod
    def mean(rl, win):
        return rl.rolling(window=win).mean()
    
    # Funzione per il calcolo della deviazione standard
    @staticmethod
    def std_dev(rl, win):
        return rl.rolling(window=win).std()
    
    # Funzione per calcolare la varianza
    @staticmethod
    def var(rl, win):
        return rl.rolling(window=win).var()
    
    # Funzione per calcolare le varie statistiche
    @staticmethod
    def stats(returns):
        # Calcolare le statistiche descrittive
        statistics = returns.describe()

        # Calcolare l'asimmetria e la curtosi
        skewness = returns.skew()
        kurtosis = returns.kurt()

        # Aggiungere l'asimmetria e la curtosi alle statistiche descrittive
        statistics.loc['skew'] = skewness
        statistics.loc['kurt'] = kurtosis

        return statistics
    
    # Funzione per calcolare le matrici di covarianza e covarianza
    @staticmethod
    def matrix(daily_pct_change):
        #Matrice di covarianza
        cov_matrix = daily_pct_change.cov()

        #Matrice di correlazione
        corr_matrix = daily_pct_change.corr()

        return cov_matrix, corr_matrix