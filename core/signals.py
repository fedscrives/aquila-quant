# signals.py
# File per calcolare le strategie d'investimento

import numpy as np
import pandas_datareader.data as web
import pandas as pd

class Signals:
    # Funzione per calcolare SMA
    @staticmethod
    def sma(all_data, window_low, window_high):
        macd = all_data.drop(columns=['High', 'Low', 'Open', 'Volume'])
        macd['SMA_LOW'] = macd['Close'].rolling(window_low).mean()
        macd['SMA_HIGH'] = macd['Close'].rolling(window_high).mean()

        macd['Price_yesterday'] = macd['Close'].shift(1)
        macd['Change'] = macd['Close'] / macd['Price_yesterday']
        macd['Invested_SMA'] = macd['Invested_SMA'] = np.where(macd['SMA_LOW'] > macd['SMA_HIGH'], 1, 0)

        sma = macd[macd['Invested_SMA'] == 1]
        sma.loc[:, 'Return'] = np.cumprod(sma['Change'])
        sma.loc[:, 'rtn'] = sma['Return'].pct_change()
        macd['rtn'] = macd['Close'] / macd['Close'].shift(1) - 1
        macd['Buy_and_hold'] = np.cumprod(1 + macd['rtn'])

        return macd

    # Funzione per calcolare EWM
    @staticmethod
    def ewm(macd, window_low, window_high):
        macd['EWM_LOW'] = macd['Close'].ewm(span=window_low, adjust=False).mean()
        macd['EWM_HIGH'] = macd['Close'].ewm(span=window_high, adjust=False).mean()
        macd['Invested_EWM'] = [1 if macd.loc[i, 'EWM_LOW'] > macd.loc[i, 'EWM_HIGH']
                                else 0 for i in macd.index]
        ewm = macd[macd['Invested_EWM'] == 1].copy()
        ewm['Price_yesterday'] = ewm['Close'].shift(1)
        ewm['Change'] = ewm['Close'] / ewm['Price_yesterday']
        ewm.loc[:, 'Return'] = np.cumprod(ewm['Change'])

        return ewm

    # Funzione per il calcolo del CAPM
    @staticmethod
    def capm(all_data, market_data, start, end):
        capm = all_data.drop(['Open', 'High', 'Low', 'Close', 'Volume', 'RS_Lordo', 'RS_Netto', 'RL'], axis=1)

        # Per il risk free scarichiamo il database della Banca della Riserva Federale di Saint Louis (FRED)
        rf = web.DataReader("TB3MS", "fred", start, end)
        rf = (1 + (rf / 100)) ** (1 / 12) - 1
        risk_free = rf['TB3MS'].iloc[-1]

        # Calcola i rendimenti percentuali giornalieri del mercato
        market_data = market_data.resample("YE").last()
        market_pct_change = market_data.pct_change().dropna()

        return risk_free, market_pct_change

    # Funzione per calcolare i beta dei titoli
    @staticmethod
    def betas(monthly_asset_returns, monthly_market_returns):

        if not isinstance(monthly_asset_returns, pd.DataFrame):
            raise TypeError("monthly_asset_returns must be a DataFrame")

        if not isinstance(monthly_market_returns, pd.Series):
            raise TypeError("monthly_market_returns must be a Series")

        aligned = monthly_asset_returns.join(
            monthly_market_returns.rename("MARKET"),
            how="inner"
        )

        market_var = aligned["MARKET"].var()

        betas = {}
        for ticker in monthly_asset_returns.columns:
            betas[ticker] = aligned[ticker].cov(aligned["MARKET"]) / market_var

        return betas



    # Funzione per il calcolo dei ritorni in base al mercato
    @staticmethod
    def ret_compare(tbill, betas, market_premium, tickers):
        # ^IRX è espresso in percentuale (es 4.5), lo dividiamo per 100
        current_tbill_rate = tbill.iloc[-1] / 100

        if not isinstance(betas, dict):
            raise TypeError("betas must be a dict {ticker: beta}")
        missing = set(tickers) - set(betas.keys())
        if missing:
            raise ValueError(f"Missing betas for: {missing}")


        # Convertiamo il tasso annuo in mensile
        tbill_monthly = (1 + current_tbill_rate) ** (1 / 12) - 1

        # Usiamo il premio di mercato mensile (già definito nel config come 0.00625)
        market_premium_monthly = market_premium

        ra_tbsp = {}
        for ticker in tickers:
            beta = betas[ticker]
            ra_tbsp[ticker] = tbill_monthly + beta * market_premium_monthly

        return ra_tbsp  # Ora i rendimenti sono mensili!