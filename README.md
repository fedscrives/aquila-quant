# AquilaQuant

**AquilaQuant** is a quantitative finance research and portfolio optimization engine designed to support data-driven investment decisions through rigorous statistical analysis, modern portfolio theory, and AI-assisted financial reporting.

The project is built with a strong focus on **methodological correctness**, **frequency consistency**, and **extensibility**, making it suitable for both academic research and real-world financial applications.

---

## Key Features

- **Market Data Ingestion**
  - Historical price data for equities and benchmarks
  - Risk-free rate integration (T-Bills)
  - Cleaned and aligned time series

- **Quantitative Analytics**
  - Daily and monthly return computation
  - Cumulative and compound returns
  - Volatility, variance, skewness, kurtosis
  - Correlation and covariance matrices

- **CAPM & Risk Metrics**
  - Monthly beta estimation vs S&P 500
  - Market premium modeling
  - Risk-free rate normalization

- **Portfolio Optimization**
  - Mean–Variance Optimization (Markowitz)
  - Past vs forward-looking portfolio comparison
  - Sharpe ratio maximization
  - Constraint-ready optimization pipeline

- **AI-Assisted Financial Analysis**
  - Automated qualitative interpretation of results
  - Structured investment reports (Markdown export)
  - Explainability-first approach

---

## Project Architecture

```text
AquilaQuant/
│
├── core/
│   ├── data_fetcher.py     # Market data ingestion
│   ├── analytics.py        # Statistical and quantitative analytics
│   ├── signals.py          # CAPM, beta, technical indicators
│   └── optimizer.py        # Portfolio optimization logic
│
├── ai_core/
│   └── client.py           # LLM-based financial analysis
│
├── reports/
│   └── Report_Analisi_*.md # Auto-generated investment reports
│
├── main.py                 # Pipeline orchestration
├── config.py               # Configuration and parameters
└── README.md



## Future Development

- Rolling beta estimation (12–36 months)
- Efficient frontier visualization
- Blended expected returns:
  - Historical mean
  - CAPM-based expectations
- Advanced risk metrics:
  - Maximum drawdown
  - Value at Risk (VaR)
  - Conditional VaR (CVaR)
- Portfolio turnover constraints
- Regime detection (bull / bear markets)
- Performance attribution analysis
- Backtesting framework with transaction costs
- Modular API for future SaaS integration
