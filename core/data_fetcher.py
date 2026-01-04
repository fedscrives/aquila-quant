# data_fetcher.py
# file per il download dei dati

import pandas as pd
import yfinance as yf

class DataFetcher:
    
    # Scarica i dati di un singolo ticker
    @staticmethod
    def data_ticker(ticker, start, end):
        df = yf.download(ticker, start, end)
        # Se yfinance restituisce colonne MultiIndex (es. [('Close', 'AAPL')]),
        # prendiamo solo il primo livello (es. 'Close')
        if isinstance(df.columns, pd.MultiIndex):
            df.columns = df.columns.get_level_values(0)
        return df

    # Scarica i dati dell'S&P500
    @staticmethod
    def sp500_close(start, end):
        # Download dati S&P500
        market_data = yf.download('^GSPC', start, end)['Close']
        return market_data

    # Scarica i dati del T-Bill
    @staticmethod
    def tbill_close(start, end):
        # Download dati T-Bill
        tbill = yf.download('^IRX', start, end)['Close']
        return tbill

    # Scarica i dati di tutti i ticker
    @staticmethod
    def get_data(tickers, start, end):
        datas = [DataFetcher.data_ticker(t, start, end) for t in tickers]
        return pd.concat(datas, keys=tickers, names=['Ticker', 'Date'])
    
    # Funzione per ritornare solo le chiusure
    @staticmethod
    def clean_data(all_data):
        just_closing_prices = all_data[['Close']].reset_index()
        daily_close = pd.pivot_table(just_closing_prices, values = 'Close', index= 'Date', columns = 'Ticker')

        return daily_close