# REPORT INVESTIMENTI - Deepseek_cloud
Titoli analizzati: AMD, UNH, COF, SPGI, NKE

=== ANALISI PERFORMANCE STORICA ===
**1. ANALISI LATEST_DATA (ULTIMI VALORI DI CHIUSURA)**

- **AMD**: Trend recente non disponibile nel sample fornito
- **UNH**: Trend recente non disponibile nel sample fornito  
- **COF**: Trend recente non disponibile nel sample fornito
- **SPGI**: Negli ultimi 5 giorni mostra volatilità con chiusura a 497.56 dopo minimo a 490.73
- **NKE**: Forte trend negativo negli ultimi giorni, passato da 67.78 a 65.63 con chiara pressione vendite

**2. ANALISI COMPOUND RETURNS (RENDIMENTI COMPOSTI ANNUALIZZATI)**

- **AMD**: 10.76% annuo - **BUONO** (vicino alla soglia 7% ma non eccellente)
- **COF**: 6.59% annuo - **BASSO** (sotto la soglia 7%, performance modesta)
- **NKE**: -1.83% annuo - **NEGATIVO** (performance deteriorata)
- **SPGI**: 0.60% annuo - **MOLTO BASSO** (praticamente piatta, inefficienza)
- **UNH**: -7.80% annuo - **MOLTO NEGATIVO** (forte underperformance)

**3. CONFRONTO CUMULATIVE RETURN vs COMPOUND RETURN**

- **AMD**: Cumulative 166.68% vs Compound 10.76% annuo
- **COF**: Cumulative 137.60% vs Compound 6.59% annuo  
- **NKE**: Cumulative 91.18% vs Compound -1.83% annuo
- **SPGI**: Cumulative 103.02% vs Compound 0.60% annuo
- **UNH**: Cumulative 66.64% vs Compound -7.80% annuo

=== ANALISI STATISTICA E RISCHIO ===
**1. STATISTICHE DESCRITTIVE DEI RENDIMENTI**

**AMD**  
Media: 150.44 | Dev Std: 49.23 | Min: 78.21 | Max: 264.33  
Skewness: 0.70 (distribuzione moderatamente asimmetrica positiva)  
Kurtosis: -0.67 (distribuzione più piatta della normale, code meno pesanti)  
*Valutazione: Elevata volatilità e ampio range di trading. Performance estrema.*

**UNH**  
Media: 377.27 | Dev Std: 92.83 | Min: 234.70 | Max: 587.56  
Skewness: 0.62 | Kurtosis: -1.02  
*Valutazione: Volatilità estrema (deviazione standard più alta). Distribuzione con code leggere.*

**COF**  
Media: 201.95 | Dev Std: 19.99 | Min: 149.12 | Max: 242.80  
Skewness: -0.46 (leggera asimmetria negativa) | Kurtosis: -0.46  
*Valutazione: Volatilità relativamente contenuta rispetto agli altri titoli.*

**NKE**  
Media: 67.69 | Dev Std: 6.76 | Min: 52.31 | Max: 79.84  
Skewness: -0.35 | Kurtosis: -0.93  
*Valutazione: Bassa volatilità e range di trading ristretto. Performance più stabile.*

**SPGI**  
Media: 507.63 | Dev Std: 25.05 | Min: 435.88 | Max: 562.06  
Skewness: 0.08 (quasi simmetrica) | Kurtosis: -0.16  
*Valutazione: Volatilità moderata con distribuzione quasi normale.*

---

**2. MATRICE DI CORRELAZIONE**

| Ticker |   AMD   |   COF   |   NKE   |  SPGI   |   UNH   |
|--------|---------|---------|---------|---------|---------|
| AMD    | 1.000000| 0.462248| 0.317822| 0.276531| 0.054853|
| COF    | 0.462248| 1.000000| 0.472277| 0.528539| 0.082230|
| NKE    | 0.317822| 0.472277| 1.000000| 0.307916| 0.010567|
| SPGI   | 0.276531| 0.528539| 0.307916| 1.000000| 0.093517|
| UNH    | 0.054853| 0.082230| 0.010567| 0.093517| 1.000000|

**Correlazione più alta:** COF-SPGI (0.5285) e COF-NKE (0.4723).  
*Problema: Forte correlazione tra titoli finanziari/rating (COF, SPGI) e consumo (NKE). Ridotta diversificazione.*

**Correlazione più bassa:** UNH-NKE (0.0106) e UNH-AMD (0.0549).  
*Vantaggio: UNH mostra correlazione quasi nulla con NKE e AMD, offrendo opportunità di diversificazione.*

---

**3. MATRICE DI COVARIANZA**

| Ticker |   AMD   |   COF   |   NKE   |  SPGI   |   UNH   |
|--------|---------|---------|---------|---------|---------|
| AMD    | 0.001498| 0.000418| 0.000316| 0.000162| 0.000065|
| COF    | 0.000418| 0.000545| 0.000283| 0.000187| 0.000058|
| NKE    | 0.000316| 0.000283| 0.000659| 0.000120| 0.000008|
| SPGI   | 0.000162| 0.000187| 0.000120| 0.000230| 0.000043|
| UNH    | 0.000065| 0.000058| 0.000008| 0.000043| 0.000925|

**Covarianza più alta:** UNH-UNH (0.000925, varianza propria) e AMD-AMD (0.001498).  
*Criticità: UNH e AMD presentano il rischio idiosincratico più elevato del portafoglio. UNH è un outlier per rischio assoluto.*

**Covarianza più bassa:** UNH-NKE (0.000008).  
*Punto di forza: La coppia UNH-NKE minimizza il rischio comovimento, ma il beneficio è marginale dato l'alto rischio individuale di UNH.*

---

**SINTESI FINALE**  
Il portafoglio è dominato dal rischio estremo di UNH e AMD. Le correlazioni non sono ottimali, con cluster di titoli (COF, SPGI, NKE) che movimentano insieme. La diversificazione è insufficiente per compensare i picchi di volatilità individuali.

=== ANALISI STRATEGIE TECNICHE ===
**Analisi Strategia Medie Mobili Semplici (SMA)**
- **Parametri**: Fast SMA 20 giorni, Slow SMA 120 giorni
- **Rendimenti**: Dati insufficienti per calcolo diretto (colonna Return non presente). La colonna *Invested_EWM* indica segnali di ingresso/uscita (1=investito, 0=non investito).
- **Performance vs Buy & Hold**: Strategia probabilmente sottoperformante dato l'elevato ritardo del slow window (120 giorni). In mercati laterali/volatili genera falsi segnali.
- **Ultimo periodo (NKE)**: Prezzo da 67.78 (15/12) a 65.63 (18/12) - **Trend ribassista**. La strategia rimane investita (Invested_EWM=1) nonostante il calo, evidenziando ritardo nel segnale di uscita.

**Analisi Strategia Medie Mobili Esponenziali (EMA)**
- **Parametri**: Fast EMA 12 giorni, Slow EMA 16 giorni
- **Rendimenti**: Ultimi valori AMD ~0.92-0.97 (gennaio), NKE ~0.52-0.54 (dicembre). Deciso underperformance vs buy & hold (NKE a -34% dal periodo iniziale).
- **Performance vs Buy & Hold**: EMA più reattiva di SMA, ma finestre troppo ravvicinate (12/16) causano eccessiva sensibilità al rumore. Rendimenti cumulative negative per NKE.
- **Ultimo periodo**: NKE in netto declino (prezzo -3.2% nelle ultime 4 sessioni), strategia rimane investita nonostante trend negativo persistente.

**Giudizio Sintetico**
Entrambe le strategie mostrano:
1. Ritardi operativi critici in fase di inversione di trend
2. Sottoperformance strutturale vs buy&hold in trend laterali/ribassisti
3. Parametrizzazioni subottimali (SMA troppo lenta, EMA troppo rumorosa)
Strategie non idonee per contesti volatili - necessitano di ottimizzazione aggressiva o abbandono.

=== OTTIMIZZAZIONE PORTAFOGLIO ===
**Analisi del Portfolio Ottimale - CIO Report**

---

**1. Risk-Free Rate (Tasso Privo di Rischio)**  
Valore: **4.50%**  
Qualsiasi investimento deve superare questo rendimento per giustificare il rischio assunto.

---

**2. Analisi Beta dei Titoli**  
- **AMD (2.86)**: Estremamente volatile, >2.8x il movimento del mercato. Altamente speculativo.  
- **UNH (-0.82)**: Beta negativo, movimenti inversi al mercato. Atipico, possibili distorsioni nei dati o caratteristiche di hedging.  
- **COF (1.07)**: Leggermente più volatile del mercato. Allineamento con l’indice di riferimento.  
- **SPGI (0.23)**: Stabile, bassa correlazione con il mercato. Difensivo.  
- **NKE (2.02)**: Molto volatile, >2x il mercato. Elevata sensibilità ai cicli economici.  
**Valutazione**: Portfolio polarizzato tra titoli iper-volatili (AMD, NKE) e difensivi (UNH, SPGI). Elevato rischio di incoerenza strategica.

---

**3. Performance del Portfolio Ottimale**  
- **Rendimento Atteso (portfolio_returns)**: **12.19%**  
  **Giudizio**: Supera il risk-free (4.50%), ma il rendimento è moderato considerando i beta elevati di AMD e NKE.  
- **Pesi (portfolio_weights)**: Distribuzione **20% per ogni titolo**.  
  **Giudizio**: Pesi artificiosamente equilibrati (probabile risultato di vincoli di ottimizzazione). Non riflette una selezione robusta, con esposizioni pari a titoli opposti (es. AMD e UNH). Inefficiente.  
- **Varianza (portfolio_variance)**: **0.0043** (~6.56% deviazione standard annua).  
  **Giudizio**: Rischio contenuto nonostante i beta estremi, grazie alla diversificazione forzata.  
- **Sharpe Ratio**: **1.19** (dato principale, il secondo valore è irrilevante).  
  **Giudizio**: Buono (>1), ma non eccellente. Compromesso tra rendimento e rischio insufficiente per giustificare i picchi di volatilità individuale.

---

**Conclusioni Critiche**  
Il portfolio è **subottimale**:  
- Equipara titoli con profili di rischio opposti (es. AMD beta 2.86 vs. UNH beta -0.82), indicando una strategia non coerente.  
- Lo Sharpe Ratio (1.19) è accettabile ma non compensa adeguatamente il rischio idiosincratico dei titoli volatili.  
- La distribuzione dei pesi al 20% suggerisce un’ottimizzazione meccanica, non supportata da una logica di selezione solida.  
**Verditto**: **Rivedere la selezione dei titoli e i vincoli di ottimizzazione**. Il rischio di sovraesposizione a volatilità estreme non è adeguatamente compensato dal rendimento atteso.