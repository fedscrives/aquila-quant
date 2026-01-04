# config.py
# File per la definizione delle variabili principali
import datetime as dt

# Nome da stampare nel report
CLIENTE = 'gpt_oos_corretto_pesos'

# LLM usato per l'analisi
LLM = 'gpt-oss:120b-cloud'


# Ticker dei titoli da tracciare
TICKERS = ['AAPL', 'MU', 'V', 'GE', 'VMC', 'EME', 'TMO', 'RCL', 'CAT']

# Data di inizio dell'analisi
START_DATE = dt.datetime(2025, 1,1)

# Data di fine dell'analisi
END_DATE = dt.datetime(2026, 1, 1)

# Numero di anni dell'analisi
YEARS = 1

# Finestra per il calcolo dei rendimenti
WINDOW = 5

# Finestra per il calcolo della media mobile veloce
SMA_LOW = 20

# Finestra per il calcolo della media mobile lenta
SMA_HIGH = 120

# Finestra per il calcolo della media mobile esponenziale veloce
EWM_LOW = 12

# Finestra per il calcolo della media mobile esponenziale lenta
EWM_HIGH = 16

# Numero di mesi per il calcolo del portfolio
FIRST_MONTHS = 108

# Media del mercato
# Per il mercato possiamo prendere o la nostra stima o una media di lungo periodo. Ipotizziamo 7,5% diviso 12 pari a 0,625%
MARTKET_PREMIUM = 0.00625

# Giorni simulazione Montecarlo
DAYS_MC = 252

# Numeri portfoli simulazione Montecarlo
N_PORTFOLIO = 100000