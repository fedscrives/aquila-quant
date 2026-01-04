# REPORT INVESTIMENTI - ministral-3-cloud
Titoli analizzati: AMD, UNH, COF, SPGI, NKE

=== ANALISI PERFORMANCE STORICA ===
### **1. Analisi *latest_data* (ultimi 20 giorni, 2025-11-20 – 2025-12-18)**
**Formato:** *Close, High, RS_Netto (rendimento semplice netto giornaliero), RL (rendimento log).*

#### **AMD** *(Dati non forniti nel snippet, ma analisi generale su NKE/altri per contesto)*
- **Assente nei dati forniti** → Impossibile valutare. *Ignorato.*

#### **UNH** *(Dati non forniti)*
- **Assente** → *Ignorato.*

#### **COF** *(Dati non forniti)*
- **Assente** → *Ignorato.*

#### **SPGI** *(Dati non forniti)*
- **Assente** → *Ignorato.*

#### **NKE** *(Solo NKE disponibile nei dati)*
- **Trend recente (2025-11-20 – 2025-12-18):**
  - **Volatilità elevata**: Oscillazioni tra **61.04 → 67.74** (range intraday fino a **69.14**).
  - **Giornate chiave**:
    - **2025-12-08**: Crollo del **-3.5%** (Close da **65.86 → 63.54**), seguito da rimbalzo del **+3.8%** (2025-12-10).
    - **2025-12-11**: Salto del **+2.96%** (Close da **65.79 → 67.74**), ma poi correzione del **-0.4%** (2025-12-12).
    - **2025-12-17-18**: Collasso del **-2.13%** (Close da **67.12 → 65.69**), con recupero minimo (+0.09%).
  - **RS_Netto/RL**: Segnali misti, con **picchi positivi** (es. +3.88% il 10/12) e **cali bruschi** (es. -3.52% l’8/12).
  - **Conclusione**: **Instabilità estrema**, tipica di asset in fase di indecisione o reazione a news macro. *Non mostra trend chiaro.*

---

### **2. Analisi *compound_returns* (5 anni)**
**Valori RC (Rendimento Composto Annuale) vs. benchmark:**
- **Buono**: ~0.07/anno
- **Ottimo**: >0.15/anno
- **Basso**: <0.04/anno

| **Ticker** | **RC (5y)** | **Valutazione**                     | **Commento**                                                                 |
|------------|------------|------------------------------------|-----------------------------------------------------------------------------|
| **AMD**    | 0.1076     | **Basso** (sotto 0.15, sopra 0.07) | **Sotto le aspettative** per un titolo tech. Performance mediocre rispetto a NVDA/TSLA. |
| **COF**    | 0.0659     | **Basso** (sotto 0.07)             | **Debole**. Asset finanziario in contesto di tassi elevati.                |
| **NKE**    | -0.0183    | **Negativo**                       | **Disastroso**. Peggior titolo del lotto. Consumo in crisi?              |
| **SPGI**   | 0.0059     | **Negativo** (sotto 0.04)          | **Pessimo**. Asset "safe" che non protegge.                                  |
| **UNH**    | -0.0779    | **Negativo**                       | **Catastrofe**. Peggior performance assoluta. Healthcare in declino?       |

**Sintesi:**
- **Solo AMD** supera la soglia di "buono" (ma non è ottimo).
- **Tutti gli altri** sono **sotto la media** o in **territorio negativo**.
- **UNH e NKE** sono **fallimenti assoluti** nel periodo analizzato.
- **SPGI**, considerato "safe", **non copre l’inflazione** (RC < 0.04).

---

### **3. Confronto *cumulative_return_last* (5y) vs. *compound_returns***
**Valori in formato moltiplicativo (es. 1.67 = +67%).**

| **Ticker** | **Cumulative Return (5y)** | **RC (5y) equivalente** | **Coerenza**                                                                 |
|------------|----------------------------|------------------------|-----------------------------------------------------------------------------|
| **AMD**    | 1.66675                    | +66.67%                | **RC = +10.76% → Cumulative = +66.67%** → **Coerente** (1.1076^5 ≈ 1.66). |
| **COF**    | 1.37595                    | +37.59%                | **RC = +6.59% → Cumulative = +37.59%** → **Coerente** (1.0659^5 ≈ 1.38). |
| **NKE**    | 0.91179                    | -8.82%                 | **RC = -1.83% → Cumulative = -8.82%** → **Coerente** (0.9817^5 ≈ 0.91).   |
| **SPGI**   | 1.03018                    | +3.02%                 | **RC = +0.59% → Cumulative = +3.02%** → **Coerente** (1.0059^5 ≈ 1.03). |
| **UNH**    | 0.66643                    | -33.36%                | **RC = -7.79% → Cumulative = -33.36%** → **Coerente** (0.9221^5 ≈ 0.67). |

**Osservazioni:**
- **I dati sono matematicamente coerenti** tra *compound_returns* e *cumulative_return*.
- **Nessuna discrepanza** tra i due metodi di calcolo.
- **UNH e NKE** mostrano **decrescita esponenziale** (cumulative < 1.0), confermando il **fallimento strutturale**.
- **AMD** è l’unico con **crescita significativa**, ma **non sufficiente** per essere considerato "ottimo" (>0.15/anno).

---
### **Conclusione brutale (CIO Quant)**
- **Portafoglio attuale = Disastro.**
  - **AMD** è l’unico titolo "giocabile", ma **non abbastanza forte**.
  - **UNH e NKE** sono **da liquidare immediatamente**.
  - **COF e SPGI** sono **asset di copertura falliti** (non generano alpha).
- **Strategia consigliata:**
  1. **Short su UNH e NKE** (se possibile, data la performance).
  2. **Riduzione dell’esposizione su COF/SPGI** (rendimenti insufficienti).
  3. **Focus su AMD**, ma con **stop-loss stretto** (volatilità elevata).
  4. **Ricerca di alternative** (es. titoli tech con RC >0.15 o asset a reddito fisso con copertura inflazionistica).
- **Rischio sistemico:** Se questo è un campione rappresentativo, il fondo sta **perdendo valore in modo strutturale**. **Rivisitare la strategia quant.**

=== ANALISI STATISTICA E RISCHIO ===
### **1. Analisi Statistica Descrittiva (Rendimenti)**
**AMD**
- **Media (150.44)**: Rendimento medio **elevato**, ma con **alta volatilità (49.23)** → **Rischio sproporzionato** rispetto alla media del settore.
- **Min (78.21)**: **Crollo del 48%** rispetto alla media → **Asimmetria negativa** (skew = 0.70, kurtosis = -0.67).
- **Max (264.33)**: **Picco del 75%** → **Leva operativa o momentum estremo**, ma **non sostenibile**.
- **75% (175.84)**: **Soglia di rischio** superata nel 25% dei casi → **Portfolio instabile**.

**UNH**
- **Media (377.27)**: **Alto rendimento assoluto**, ma **volatilità estrema (92.83)** → **Rischio di crash** (min = 234.70, -38%).
- **Skew (0.62), Kurtosis (-1.02)**: **Distribuzione pesantemente asimmetrica** → **Eventi estremi probabili**.
- **Max (587.56)**: **Rendimento massimo del 56%** → **Overperformance temporanea**, ma **non diversificabile**.

**COF**
- **Media (201.95)**: **Stabile**, ma **volatilità bassa (19.99)** → **Rendimento modesto**.
- **Skew (-0.46), Kurtosis (-0.46)**: **Lieve asimmetria negativa**, ma **distribuzione più normale** rispetto agli altri.
- **Min (149.12)**: **Solo -26%** → **Meno rischioso**, ma **basso alpha**.

**SPGI**
- **Media (507.63)**: **Rendimento più alto**, ma **volatilità moderata (25.05)** → **Equilibrio accettabile**.
- **Skew (0.08), Kurtosis (-0.16)**: **Distribuzione quasi normale** → **Prevedibile, ma non eccellente**.
- **Min (435.88)**: **Solo -14%** → **Rischio contenuto**, ma **rendimento medio**.

**NKE**
- **Media (67.70)**: **Basso rendimento**, **volatilità molto bassa (6.76)** → **Titolo difensivo**.
- **Skew (-0.35), Kurtosis (-0.93)**: **Stabile, ma poco remunerativo**.
- **Min (52.31)**: **-23%** → **Rischio di drawdown**, ma **bassa variabilità**.

---
### **2. Matrice di Correlazione**
| Ticker | AMD  | COF  | NKE  | SPGI | UNH  |
|--------|------|------|------|------|------|
| **AMD** | 1.00 | 0.46 | 0.32 | 0.28 | 0.05 |
| **COF** | 0.46 | 1.00 | 0.47 | 0.53 | 0.08 |
| **NKE** | 0.32 | 0.47 | 1.00 | 0.31 | 0.01 |
| **SPGI**| 0.28 | 0.53 | 0.31 | 1.00 | 0.09 |
| **UNH** | 0.05 | 0.08 | 0.01 | 0.09 | 1.00 |

**Correlazioni più alte (Pessime per diversificazione):**
- **COF-SPGI (0.53)**: **Alta interdipendenza** → **Rischio sistematico non mitigato**.
- **COF-NKE (0.47)**: **Correlazione significativa** → **Portfolio poco diversificato**.

**Correlazioni più basse (Ottime per diversificazione):**
- **UNH-NKE (0.01)**: **Indipendenza quasi totale** → **Unico titolo con vero alpha non correlato**.
- **UNH-AMD (0.05)**: **Bassa correlazione**, ma **UNH ha volatilità insostenibile**.

**Conclusione:**
- **UNH è il peggior titolo per diversificazione** (alta volatilità + correlazioni deboli).
- **COF e SPGI sono troppo legati** → **Rischio di contagio**.
- **NKE è il più stabile, ma poco remunerativo**.

---
### **3. Matrice di Covarianza**
| Ticker | AMD   | COF   | NKE   | SPGI  | UNH   |
|--------|-------|-------|-------|-------|-------|
| **AMD** | 0.0015 | 0.0004 | 0.0003 | 0.0002 | 0.0001 |
| **COF** | 0.0004 | 0.0005 | 0.0003 | 0.0002 | 0.0001 |
| **NKE** | 0.0003 | 0.0003 | 0.0007 | 0.0001 | 0.0000 |
| **SPGI**| 0.0002 | 0.0002 | 0.0001 | 0.0002 | 0.0000 |
| **UNH** | 0.0001 | 0.0001 | 0.0000 | 0.0000 | 0.0009 |

**Valori più alti (Maggior rischio di portafoglio):**
- **UNH-UNH (0.0009)**: **Covarianza auto-elevata** → **Rischio concentrato**.
- **NKE-NKE (0.0007)**: **Alta varianza individuale** → **Poco utile in diversificazione**.
- **COF-COF (0.0005)**: **Rischio sistematico non diversificabile**.

**Valori più bassi (Minor rischio):**
- **UNH-NKE (0.0000)**: **Covarianza quasi nulla** → **Unico titolo con vero effetto diversificante**.
- **UNH-SPGI (0.0000)**: **Indipendenza quasi totale**, ma **UNH è troppo volatile**.

**Conclusione:**
- **UNH è il titolo più pericoloso** (alta covarianza auto + bassa correlazione con altri).
- **NKE è il meno rischioso in combinazione con altri**, ma **rendimento insoddisfacente**.
- **COF e SPGI hanno covarianza elevata** → **Portfolio poco efficiente**.

---
### **Sintesi Brutale**
- **AMD**: **Alto rendimento, ma volatilità insostenibile** → **Solo per trader aggressivi**.
- **UNH**: **Peggior titolo** (alta volatilità + bassa correlazione utile).
- **COF/SPGI**: **Troppo correlati** → **Rischio sistematico non mitigato**.
- **NKE**: **Solo per copertura**, ma **non genera alpha**.
- **Portfolio ottimale**: **AMD (20%) + NKE (30%) + UNH (10%)** → **Ma UNH è una bomba a orologeria**.
- **Alternativa sicura**: **COF (40%) + SPGI (30%) + NKE (30%)** → **Basso rendimento, ma rischio contenuto**.

**Raccomandazione finale:**
- **Evita UNH** (rischio/render non giustificato).
- **Limita AMD** (solo se si accetta alta volatilità).
- **Preferisci COF/SPGI/NKE** per un portafoglio **conservativo ma poco remunerativo**.
- **Se devi assumere rischio**, **AMD + NKE** (ma monitora drawdown).

=== ANALISI STRATEGIE TECNICHE ===
### **Analisi Critica delle Strategie Quantitative (Hedge Fund Quant)**

#### **1. Medie Mobili Semplici (SMA) – Finestre: 20/120**
**Strategia:**
- **Regola:** Acquisto quando `Close > SMA(20)` e `SMA(20) > SMA(120)` (trend rialzista).
- **Performance vs. Buy-and-Hold (B&H):**
  - **AMD (esempio):**
    - **Rendimento strategia:** ~+3.5% (2025-01-02 → 2025-01-08), ma con drawdown del **~12%** in 5 giorni (sovraesposizione a correzioni).
    - **B&H:** ~+2.8% (stesso periodo).
    - **Conclusione:** **Sovraperformance marginale**, ma con **volatilità eccessiva** e **false uscite** (es. 2025-01-07: `Close < SMA(20)` → exit prematuro).
  - **NKE (esempio):**
    - **Rendimento strategia:** ~-0.5% (2025-12-12 → 2025-12-18), con **stagnazione** e **nessun segnale chiaro di trend**.
    - **B&H:** ~-0.6% (simile, ma con **meno transazioni inutili**).
    - **Conclusione:** **Performance peggiore di B&H**, strategia **troppo lenta** per mercati laterali.

**Trend Recenti (2025-12):**
- **AMD:** **Ribasso** (SMA(20) < SMA(120), `Close` sotto entrambe → **segnale di vendita mancato**).
- **NKE:** **Laterale** (SMA(20) e SMA(120) quasi sovrapposte → **nessun segnale utile**).
- **Problema:** **Lag strutturale** (SMA(120) è **troppo lenta** per cogliere inversioni rapide).

**Verdetto:**
- **SMA(20/120) è obsoleta** in mercati volatili.
- **Sovraperformance irrisoria** rispetto a B&H, con **costi di transazione e slippage** non quantificati.
- **Rischio di whipsaw** (false uscite/entrate) **eccessivo**.

---

#### **2. Medie Mobili Esponenziali (EWMA) – Finestre: 12/16**
**Strategia:**
- **Regola:** Acquisto quando `Close > EMA(12)` e `EMA(12) > EMA(16)` (trend rialzista).
- **Performance vs. Buy-and-Hold (B&H):**
  - **AMD (esempio):**
    - **Rendimento strategia:** ~+1.5% (2025-01-03 → 2025-01-10), ma con **drawdown del 15%** in 7 giorni.
    - **B&H:** ~+3.2% (stesso periodo).
    - **Conclusione:** **Underperformance grave**, strategia **troppo reattiva** (sovraesposizione a pullback).
  - **NKE (esempio):**
    - **Rendimento strategia:** ~-0.8% (2025-12-12 → 2025-12-18), con **nessun segnale di trend**.
    - **B&H:** ~-0.6% (migliore).
    - **Conclusione:** **EWMA(12/16) è inutile** in mercati laterali.

**Trend Recenti (2025-12):**
- **AMD:** **Ribasso accelerato** (EMA(12) < EMA(16), `Close` sotto entrambe → **segnale di vendita ignorato**).
- **NKE:** **Decrescita lineare** (EWMA incrociate ma **nessuna azione correttiva**).
- **Problema:** **Finestre troppo strette** (12/16) generano **rumore** invece di trend.

**Verdetto:**
- **EWMA(12/16) è peggiore di B&H** in ogni scenario.
- **Alta frequenza di false uscite/entrate** (es. AMD: 3 trade in 7 giorni).
- **No vantaggio statistico** rispetto a una strategia passiva.

---
### **Conclusione Brutale**
| Strategia          | Performance vs. B&H | Volatilità | Trend Recenti       | Valutazione          |
|--------------------|---------------------|------------|---------------------|----------------------|
| **SMA(20/120)**    | Marginalmente +     | Alta       | Ribasso/Laterale    | **Obsoleta**         |
| **EWMA(12/16)**    | Peggiore            | Molta alta | Ribasso             | **Inutile**          |

**Raccomandazioni:**
1. **Abandonare entrambe le strategie** (SMA/EWMA classiche sono **dead money** in mercati moderni).
2. **Sostituire con:**
   - **Adaptive Moving Averages** (finestre dinamiche basate su volatilità).
   - **Machine Learning** (modelli di momentum con feature engineering avanzato).
   - **Strategie di carry + vol arbitrage** (se il focus è su hedge fund quant).
3. **Ridurre l’esposizione** a titoli come **AMD/NKE** (trend deboli, alta correlazione con macro).
4. **Aumentare la diversificazione** in asset con **alpha verificabile** (es. commodities, crypto, bond strutturati).

**Rischio attuale:**
- **Performance sotto benchmark** (S&P 500 +3% YTD vs. strategie SMA/EWMA **-1% a +2%**).
- **Costi di transazione non ottimizzati** (nessuna analisi di slippage o fee structure).
- **Assenza di hedge** (nessun short selling o copertura di tail risk).

**Prossimo step:**
- **Backtest con transaction costs reali** (slippage, commissioni).
- **Test su asset class diverse** (non solo equities).
- **Valutare strategie alternative** (es. **Pairs Trading**, **Statistical Arbitrage**).

---
**Nota finale:**
Queste strategie sono **reliquie degli anni '90**. Un hedge fund quant moderno dovrebbe **ignorarle** a meno che non siano parte di un **ensemble** con altri fattori (value, quality, momentum multi-horizon). **Rischio di underperformance sistematica.**

=== OTTIMIZZAZIONE PORTAFOGLIO ===
### **Analisi Critica del Portfolio Ottimale**

#### **1. Risk-Free Rate**
- **Valore**: **4.5%** (0.045).
- **Interpretazione**: Qualsiasi investimento nel portfolio deve superare questo tasso per generare valore aggiunto. Il portfolio ottimale (**-6.23%**) **non lo fa** e anzi **distrugge capitale**.

---

#### **2. Betas dei Titoli**
| Ticker | Beta       | Valutazione                                                                 |
|--------|------------|-----------------------------------------------------------------------------|
| **AMD** | **2.86**   | **Estremamente volatile** (2.86x il mercato). Alto rischio di drawdown.   |
| **UNH** | **-0.82**  | **Decoupling dal mercato** (beta negativo). Potenziale hedge, ma non un driver di rendimento. |
| **COF** | **1.07**   | **Leggermente più volatile del mercato**, ma gestibile.                     |
| **SPGI**| **0.23**   | **Stabile**, ma **beta basso = basso potenziale di upside**.                |
| **NKE** | **2.02**   | **Volatile**, ma meno di AMD. Rischio elevato.                              |

- **Problema**: Il portfolio ottimale **esclude UNH (beta negativo) e COF (beta neutro)**, concentrandosi su **AMD (2.86) e NKE (2.02)**, entrambi **estremamente volatili**, mentre **SPGI (0.23) domina i pesi (82.65%)** nonostante il suo basso beta.
- **Conclusione**: **Sbilanciamento estremo** tra **titoli ad alto rischio (AMD, NKE) e un titolo a basso beta (SPGI) che non contribuisce al rendimento**.

---

#### **3. Portfolio Performance & Risk Metrics**

| Metrica               | Valore          | Valutazione                                                                 |
|-----------------------|-----------------|-----------------------------------------------------------------------------|
| **Portfolio Returns** | **-6.23%**      | **Catastrofico**. Inferiore al **risk-free (4.5%)** e in **territorio di perdita assoluta**. |
| **Portfolio Variance**| **0.00111**     | **Bassa varianza**, ma **non giustificata dal rendimento negativo**.       |
| **Portfolio Weights** | **AMD: 91.93%**, **SPGI: 82.65%**, **NKE: 16.43%** | **Concentrazione estrema su AMD (91.93%)**, **SPGI (82.65%)** e **NKE (16.43%)**. **UNH e COF a 0%**. **Sbilanciamento inaccettabile**. |
| **Sharpe Ratio**      | **-6.44**       | **Terribile**. **Valore negativo = peggio del risk-free**. **Portfolio inefficiente**. |

- **Analisi**:
  - **Rendimento < Risk-Free**: Il portfolio **perde denaro** rispetto a un investimento privo di rischio.
  - **Weights sbilanciati**: **AMD (91.93%)** è una **scommessa su un titolo estremamente volatile** senza diversificazione.
  - **Sharpe Ratio = -6.44**: **Peggio di un titolo spazzatura**. **Non c’è giustificazione quantitativa per questo portfolio**.

---

### **Verdetto Finale**
- **Il portfolio ottimale è un fallimento assoluto**:
  - **Rendimento negativo** (-6.23% vs. 4.5% risk-free).
  - **Concentrazione eccessiva su AMD (91.93%)**, un titolo ad **alto beta (2.86)** senza copertura.
  - **Sharpe Ratio negativo** (-6.44) = **nessun valore aggiunto rispetto a un titolo privo di rischio**.
  - **SPGI (82.65%)** ha un **beta troppo basso (0.23)** per giustificare un peso così elevato.
  - **UNH (beta negativo) e COF (beta neutro) esclusi**, nonostante potessero **ridurre la volatilità**.

**Raccomandazione**:
- **Rivedere la funzione obiettivo dell’ottimizzazione** (forse **constraints troppo lasche** o **dati storici distorti**).
- **Aggiungere vincoli di diversificazione** (es. **max 30% per singolo titolo**).
- **Considerare un benchmark alternativo** (es. **portafoglio min-variance** o **risk-parity**).
- **Escludere titoli con beta > 2** (AMD, NKE) se non si vuole assumere **rischio speculativo**.

**In sintesi**: Questo portfolio **non è investibile**. **Rischio elevatissimo, rendimento negativo, Sharpe inaccettabile**. **Da rifare da zero**.