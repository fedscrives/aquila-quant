"""
API FastAPI per Aquila-Quant
Espone endpoint per l'analisi finanziaria
"""

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
from typing import List, Optional
import datetime as dt
import logging
import os
import numpy as np

# Import della logica esistente
from core import (data_fetcher as df,
                  analytics as an,
                  signals as s,
                  optimizer as op)
from ai_core import client as cl

# Configurazione logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Inizializzazione FastAPI
app = FastAPI(
    title="Aquila-Quant API",
    description="API per analisi finanziaria avanzata con AI",
    version="1.0.0"
)

# Configurazione CORS per permettere richieste dal frontend Angular
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:4200"],  # Porta di default di Angular
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# ===== MODELLI PYDANTIC =====

class AnalysisRequest(BaseModel):
    """Richiesta di analisi finanziaria"""
    tickers: List[str] = Field(..., description="Lista di ticker da analizzare", example=["AAPL", "MSFT", "GOOGL"])
    start_date: str = Field(..., description="Data di inizio (YYYY-MM-DD)", example="2020-01-01")
    end_date: str = Field(..., description="Data di fine (YYYY-MM-DD)", example="2025-12-31")
    report_name: str = Field(..., description="Nome del report da generare", example="Portfolio_Tech_2025")
    llm_model: Optional[str] = Field(default="gpt-oss:20b-cloud", description="Modello LLM da usare")
    
    # Parametri opzionali con valori di default
    window: int = Field(default=5, description="Finestra per calcolo rendimenti")
    sma_low: int = Field(default=120, description="Finestra SMA veloce")
    sma_high: int = Field(default=200, description="Finestra SMA lenta")
    ewm_low: int = Field(default=16, description="Finestra EWM veloce")
    ewm_high: int = Field(default=32, description="Finestra EWM lenta")
    first_months: int = Field(default=108, description="Mesi per calcolo portfolio")
    market_premium: float = Field(default=0.00625, description="Premio di mercato mensile")


class AnalysisResponse(BaseModel):
    """Risposta dell'analisi"""
    status: str
    message: str
    report_path: Optional[str] = None
    report_content: Optional[str] = None


# ===== ENDPOINT API =====

@app.get("/")
async def root():
    """Endpoint di benvenuto"""
    return {
        "message": "Benvenuto in Aquila-Quant API",
        "version": "1.0.0",
        "docs": "/docs"
    }


@app.get("/health")
async def health_check():
    """Verifica stato dell'API"""
    return {"status": "healthy", "timestamp": dt.datetime.now().isoformat()}


@app.post("/analyze", response_model=AnalysisResponse)
async def run_analysis(request: AnalysisRequest):
    """
    Esegue l'analisi finanziaria completa
    
    - **tickers**: Lista di simboli azionari da analizzare
    - **start_date**: Data di inizio analisi
    - **end_date**: Data di fine analisi
    - **report_name**: Nome del report da salvare
    """
    try:
        logger.info(f"Avvio analisi per: {request.tickers}")
        
        # Conversione date
        start_dt = dt.datetime.strptime(request.start_date, "%Y-%m-%d")
        end_dt = dt.datetime.strptime(request.end_date, "%Y-%m-%d")
        years = (end_dt - start_dt).days / 365.25
        
        # 1. DATA INGESTION
        logger.info("Fase 1: Scaricamento dati...")
        data = df.DataFetcher.get_data(request.tickers, start_dt, end_dt)
        chiusure = df.DataFetcher.clean_data(data)
        sp500 = df.DataFetcher.sp500_close(start_dt, end_dt)
        tbill = df.DataFetcher.tbill_close(start_dt, end_dt)
        
        # 2. QUANTITATIVE ANALYTICS
        logger.info("Fase 2: Analisi quantitativa...")
        pct = an.Analytics.pct_change(chiusure)
        monthly_ret, _ = op.Optimizer.first_months(pct, chiusure, end_dt, request.first_months)
        expt_ret = monthly_ret.mean()
        
        rend_comp = an.Analytics.comp_ret(chiusure)
        _, rend_cum_last = an.Analytics.cum_ret(pct)
        rs_lordo, rs_netto, rl = an.Analytics.returns(data)
        media = an.Analytics.mean(rl, request.window)
        std = an.Analytics.std_dev(rl, request.window)
        var = an.Analytics.var(rl, request.window)
        stats = an.Analytics.stats(pct)
        _, corr = an.Analytics.matrix(monthly_ret)
        cov = monthly_ret.cov()
        
        # 3. SIGNAL GENERATION
        logger.info("Fase 3: Generazione segnali...")
        sma = s.Signals.sma(data, request.sma_low, request.sma_high)
        ewm = s.Signals.ewm(sma, request.ewm_low, request.ewm_high)
        risk_free, market_pct = s.Signals.capm(data, sp500, start_dt, end_dt)
        sp500_monthly = sp500["^GSPC"].resample("M").last().pct_change().dropna()
        betas = s.Signals.betas(monthly_ret, sp500_monthly)
        ret_compare = s.Signals.ret_compare(tbill, betas, request.market_premium, request.tickers)
        
        # 4. PORTFOLIO OPTIMIZATION
        logger.info("Fase 4: Ottimizzazione portafoglio...")
        opt_past, opt_future, xpt_ret_past, cov_past = \
            op.Optimizer.optimal_weights(monthly_ret, request.tickers, ret_compare)
        
        var_pst = op.Optimizer.portfolio_variance(opt_past, cov_past)
        var_ftr = op.Optimizer.portfolio_variance(opt_future, cov_past)
        
        sharpe_past = xpt_ret_past @ opt_past / np.sqrt(var_pst)
        sharpe_future = xpt_ret_past @ opt_future / np.sqrt(var_ftr)
        
        if sharpe_future > sharpe_past:
            best_weights = opt_future
            var_port_best = var_ftr
            best_sharpe = sharpe_future
        else:
            best_weights = opt_past
            var_port_best = var_pst
            best_sharpe = sharpe_past
        
        rit_port_best = op.Optimizer.portfolio_return(best_weights, xpt_ret_past)
        best_pesi = op.Optimizer.best_weights(request.tickers, best_weights)
        
        # 5. AI CRITICAL ANALYSIS
        logger.info("Fase 5: Analisi AI...")
        out_data = cl.LlmClient.evaluate_data(
            data.groupby(level=0).tail(22), 
            rend_comp, 
            rend_cum_last, 
            request.llm_model, 
            request.tickers, 
            int(years)
        )
        out_an = cl.LlmClient.evaluate_analytics(stats, corr, cov, request.llm_model, request.tickers)
        out_sig = cl.LlmClient.evaluate_signals(
            sma, ewm, request.llm_model, 
            request.sma_low, request.sma_high, 
            request.ewm_low, request.ewm_high
        )
        out_opt = cl.LlmClient.evaluate_optimizer(
            risk_free, betas, rit_port_best, 
            best_pesi, var_port_best, 
            request.llm_model, request.tickers, best_sharpe
        )
        
        report_completo = (
            "=== ANALISI PERFORMANCE STORICA ===\n" + out_data + "\n\n" +
            "=== ANALISI STATISTICA E RISCHIO ===\n" + out_an + "\n\n" +
            "=== ANALISI STRATEGIE TECNICHE ===\n" + out_sig + "\n\n" +
            "=== OTTIMIZZAZIONE PORTAFOGLIO ===\n" + out_opt
        )
        
        # 6. SALVATAGGIO REPORT
        folder_name = "reports"
        if not os.path.exists(folder_name):
            os.makedirs(folder_name)
        
        filename = f"Report_{request.report_name}.md"
        file_path = os.path.join(folder_name, filename)
        
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(f"# REPORT INVESTIMENTI - {request.report_name}\n")
            f.write(f"Titoli analizzati: {', '.join(request.tickers)}\n\n")
            f.write(report_completo)
        
        logger.info(f"Report salvato: {file_path}")
        
        return AnalysisResponse(
            status="success",
            message=f"Analisi completata con successo per {len(request.tickers)} titoli",
            report_path=file_path,
            report_content=report_completo
        )
        
    except Exception as e:
        logger.error(f"Errore durante l'analisi: {e}", exc_info=True)
        raise HTTPException(status_code=500, detail=f"Errore durante l'analisi: {str(e)}")


@app.get("/reports")
async def list_reports():
    """Elenca tutti i report disponibili"""
    try:
        folder_name = "reports"
        if not os.path.exists(folder_name):
            return {"reports": []}
        
        reports = [f for f in os.listdir(folder_name) if f.endswith('.md')]
        return {"reports": reports, "count": len(reports)}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/reports/{report_name}")
async def get_report(report_name: str):
    """Recupera il contenuto di un report specifico"""
    try:
        file_path = os.path.join("reports", report_name)
        if not os.path.exists(file_path):
            raise HTTPException(status_code=404, detail="Report non trovato")
        
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
        
        return {"report_name": report_name, "content": content}
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)
