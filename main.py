# main.py
# File per l'avvio

import logging
import numpy as np
import os
from core import (data_fetcher as df,
                  analytics as an,
                  signals as s,
                  optimizer as op)
from ai_core import client as cl
from config import *

# Configurazione del logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

print("="*50)
print("   INVESTMENT ANALYSIS TOOL v0.1 - AI POWERED")
print("="*50)

class FinancialAnalyzer:
    def __init__(self):
        self.results = {}
        logger.info("Analizzatore Finanziario Inizializzato")

    def run_pipeline(self):
        try:
            # 1. DATA INGESTION
            logger.info(f"Scaricamento dati per: {TICKERS}")
            self.data = df.DataFetcher.get_data(TICKERS, START_DATE, END_DATE)
            self.chiusure = df.DataFetcher.clean_data(self.data)
            self.sp500 = df.DataFetcher.sp500_close(START_DATE, END_DATE)
            self.tbill = df.DataFetcher.tbill_close(START_DATE, END_DATE)

            # 2. QUANTITATIVE ANALYTICS
            logger.info("Esecuzione analisi quantitativa...")
            self.pct = an.Analytics.pct_change(self.chiusure)

            self.monthly_ret, _ = op.Optimizer.first_months(self.pct, self.chiusure, END_DATE, FIRST_MONTHS)

            self.expt_ret = self.monthly_ret.mean()

            # Rendimento composto dei titoli
            self.rend_comp = an.Analytics.comp_ret(self.chiusure)
            # Rendimento cumulato dei titoli
            _, self.rend_cum_last = an.Analytics.cum_ret(self.pct)
            print(self.rend_cum_last)
            # Rendimento lordo, netto e logaritmico dei titoli
            self.rs_lordo, self.rs_netto, self.rl = an.Analytics.returns(self.data)
            # Media dei titoli
            self.media = an.Analytics.mean(self.rl, WINDOW)
            # Deviazione standard dei titoli
            self.std = an.Analytics.std_dev(self.rl, WINDOW)
            # Varianza dei titoli
            self.var = an.Analytics.var(self.rl, WINDOW)
            self.stats = an.Analytics.stats(self.pct)
            
            _, self.corr = an.Analytics.matrix(self.monthly_ret)
            self.cov = self.monthly_ret.cov()


            # Salviamo i risultati per l'IA
            #_, self.results['rend_com'] = an.Analytics.clean_com_ret(YEARS, self.chiusure)

            # 3. SIGNAL GENERATION
            logger.info("Calcolo indicatori tecnici e Beta...")
            self.sma = s.Signals.sma(self.data, SMA_LOW, SMA_HIGH)
            self.ewm = s.Signals.ewm(self.sma, EWM_LOW, EWM_HIGH)
            # Risk Free e variazione percentile di S&P500
            self.risk_free, self.market_pct = s.Signals.capm(self.data, self.sp500, START_DATE, END_DATE)
            self.sp500_monthly = (
                self.sp500["^GSPC"]
                .resample("M")
                .last()
                .pct_change()
                .dropna()
            )
            print("monthly_ret type:", type(self.monthly_ret))
            print(self.monthly_ret.head())

            print("sp500_monthly type:", type(self.sp500_monthly))
            print(self.sp500_monthly.head())


            self.betas = s.Signals.betas(self.monthly_ret, self.sp500_monthly)
            self.ret_compare = s.Signals.ret_compare(self.tbill, self.betas, MARTKET_PREMIUM, TICKERS)

            # 4. PORTFOLIO OPTIMIZATION
            logger.info("Ottimizzazione portafoglio (Markowitz)...")
            
            self.opt_past, self.opt_future, self.xpt_ret_past, self.cov_past = \
                op.Optimizer.optimal_weights(self.monthly_ret, TICKERS, self.ret_compare)

            self.var_pst = op.Optimizer.portfolio_variance(self.opt_past, self.cov_past)
            self.var_ftr = op.Optimizer.portfolio_variance(self.opt_future, self.cov_past)

            self.sharpe_past = self.xpt_ret_past @ self.opt_past / np.sqrt(self.var_pst)
            self.sharpe_future = self.xpt_ret_past @ self.opt_future / np.sqrt(self.var_ftr)

            if self.sharpe_future > self.sharpe_past:
                self.best_weights = self.opt_future
                self.var_port_best = self.var_ftr
            else:
                self.best_weights = self.opt_past
                self.var_port_best = self.var_pst

            if self.sharpe_future > self.sharpe_past:
                self.best_sharpe = self.sharpe_future
            else:
                self.best_sharpe = self.sharpe_past

            # Ritorni attesi miglior portfolio
            self.rit_port_best = op.Optimizer.portfolio_return(self.best_weights, self.xpt_ret_past)
            # Pesi del miglior portfolio
            self.best_pesi = op.Optimizer.best_weights(TICKERS, self.best_weights)
            # Varianza del miglior portfolio
            self.var_port_best = op.Optimizer.portfolio_variance(self.best_weights, self.cov_past)
            
            print("Risk-free monthly:", self.risk_free)
            print("Risk-free annualized:", (1 + self.risk_free)**12 - 1)


            # 5. AI CRITICAL ANALYSIS
            logger.info("Avvio analisi critica tramite LLM...")
            self.final_report = self._run_ai_analysis()

            self._save_report()

        except Exception as e:
            logger.error(f"Errore critico durante la pipeline: {e}", exc_info=True)

    def _run_ai_analysis(self):
        # Qui chiami i metodi del tuo LlmClient in modo ordinato
        self.out_data = cl.LlmClient.evaluate_data(self.data.groupby(level=0).tail(22), self.rend_comp, self.rend_cum_last, LLM, TICKERS, YEARS)
        self.out_an = cl.LlmClient.evaluate_analytics(self.stats, self.corr, self.cov, LLM, TICKERS)
        self.out_sig = cl.LlmClient.evaluate_signals(self.sma, self.ewm, LLM, SMA_LOW, SMA_HIGH, EWM_LOW, EWM_HIGH)
        self.out_opt = cl.LlmClient.evaluate_optimizer(self.risk_free, self.betas, self.rit_port_best, self.best_pesi, self.var_port_best, LLM, TICKERS, self.best_sharpe)
        report_completo = (
                "=== ANALISI PERFORMANCE STORICA ===\n" + self.out_data + "\n\n" +
                "=== ANALISI STATISTICA E RISCHIO ===\n" + self.out_an + "\n\n" +
                "=== ANALISI STRATEGIE TECNICHE ===\n" + self.out_sig + "\n\n" +
                "=== OTTIMIZZAZIONE PORTAFOGLIO ===\n" + self.out_opt
        )
        return report_completo

    def _save_report(self):
        folder_name = "reports"

        # Creazione cartella se non esiste già
        if not os.path.exists(folder_name):
            os.makedirs(folder_name)
            logger.info(f"Cartella '{folder_name}' creata.")

        # Definizione percorso completo del file
        # os.path.join gestisce correttamente gli slash (/ o \) a seconda del sistema operativo
        filename = f"Report_Analisi_{CLIENTE}.md"
        file_path = os.path.join(folder_name, filename)

        try:
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(f"# REPORT INVESTIMENTI - {CLIENTE}\n")
                f.write(f"Titoli analizzati: {', '.join(TICKERS)}\n\n")
                f.write(self.final_report)
            logger.info(f"Report salvato con successo in: {file_path}")
        except Exception as e:
            logger.error(f"Errore durante il salvataggio del report: {e}")

if __name__ == "__main__":
    analyzer = FinancialAnalyzer()
    analyzer.run_pipeline()