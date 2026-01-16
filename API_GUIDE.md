# Guida API - Aquila-Quant Backend

## Avvio del Server

Il server API è già in esecuzione su `http://localhost:8000`

Per avviarlo manualmente:
```bash
source .venv/bin/activate
uvicorn api:app --reload --host 0.0.0.0 --port 8000
```

## Documentazione Interattiva

FastAPI genera automaticamente la documentazione interattiva:

- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

Puoi testare tutti gli endpoint direttamente dal browser!

## Endpoint Disponibili

### 1. Health Check
```bash
GET http://localhost:8000/health
```

### 2. Esegui Analisi Completa
```bash
POST http://localhost:8000/analyze
Content-Type: application/json

{
  "tickers": ["AAPL", "MSFT", "GOOGL"],
  "start_date": "2020-01-01",
  "end_date": "2025-12-31",
  "report_name": "Portfolio_Tech_2025",
  "llm_model": "gpt-oss:20b-cloud"
}
```

**Parametri opzionali** (con valori di default):
- `window`: 5
- `sma_low`: 120
- `sma_high`: 200
- `ewm_low`: 16
- `ewm_high`: 32
- `first_months`: 108
- `market_premium`: 0.00625

### 3. Lista Report Salvati
```bash
GET http://localhost:8000/reports
```

### 4. Recupera un Report Specifico
```bash
GET http://localhost:8000/reports/Report_Portfolio_Tech_2025.md
```

## Test con cURL

### Test rapido:
```bash
curl http://localhost:8000/health
```

### Esegui un'analisi:
```bash
curl -X POST "http://localhost:8000/analyze" \
  -H "Content-Type: application/json" \
  -d '{
    "tickers": ["AAPL", "MSFT"],
    "start_date": "2023-01-01",
    "end_date": "2024-01-01",
    "report_name": "Test_Report"
  }'
```

## CORS

Il server è configurato per accettare richieste da:
- `http://localhost:4200` (Angular dev server)

Se hai bisogno di altri domini, modifica la lista in `api.py`:
```python
allow_origins=["http://localhost:4200", "http://altro-dominio.com"]
```

## Formato Risposta

### Successo (200):
```json
{
  "status": "success",
  "message": "Analisi completata con successo per 3 titoli",
  "report_path": "reports/Report_Portfolio_Tech_2025.md",
  "report_content": "=== ANALISI PERFORMANCE STORICA ===\n..."
}
```

### Errore (500):
```json
{
  "detail": "Errore durante l'analisi: <messaggio>"
}
```

## Prossimi Passi

Ora che il backend è pronto, puoi:
1. Testare gli endpoint con Swagger UI
2. Creare il frontend Angular che consumerà questa API
3. Implementare autenticazione (JWT) se necessario
