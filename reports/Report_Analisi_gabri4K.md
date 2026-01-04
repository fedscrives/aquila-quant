# REPORT INVESTIMENTI - gabri4K
Titoli analizzati: NVDA, AAPL, SLDP

=== ANALISI PERFORMANCE STORICA ===
**1. latest_data – sintesi per ticker**  

| Ticker | Trend principale (ultimi 5‑6 giorni) | Note operative (RS_Lordo / RS_Netto) |
|--------|-------------------------------------|--------------------------------------|
| **NVDA** | Il prezzo è sceso dal picco di *115,38* (02‑05) a *114,72* (06‑05), con una lieve flessione dei volumi. Il movimento è marginale (< 1 %). | RS = 0,998 (alla chiusura del 06‑05): quasi neutro. Il valore netto è leggermente negativo (‑0,0023), indicando una piccola pressione di vendita rispetto al benchmark. |
| **AAPL** | Dopo un rialzo a *200,43* (fine periodo) il titolo è rimasto sostanzialmente stabile – il prezzo di chiusura del 30‑05 è *200,43* con variazioni giornaliere inferiori allo 0,5 %. | RS ≈ 0,999 (corrispondente a un ritorno quasi nullo). Il segnale netto è leggermente positivo (≈ +0,001), ma non significativo. |
| **SLDP** | Il titolo ha subito una contrazione marcata: da *1,85* (28‑05) a *1,70* (30‑05). Il volume è diminuito drasticamente, segnale di scarso interesse. | RS = 0,929 (30‑05): forte deterioramento. RS_Netto è negativo (‑0,071), confermando la perdita di valore. |

**2. compound_returns – valutazione per ticker**  

| Ticker | RC (rendimento composto) | Interpretazione (basata su soglie annue) | Commento di performance |
|--------|--------------------------|-------------------------------------------|------------------------|
| **NVDA** | **0.17543** (≈ 17,5 % annuo) | **Eccellente** (> 0,15) | Il valore è ben sopra la media di mercato; la base di crescita è solida nonostante il recente consolidamento. |
| **AAPL** | **0.03999** (≈ 4,0 % annuo) | **Basso** (< 0,04) – appena sulla soglia | Rendimento stagnante, incompatibile con il profilo di alto‑capitalizzazione tecnologica. |
| **SLDP** | **‑0.09827** (≈ ‑9,8 % annuo) | **Pessimo** (sotto 0,04, negativo) | Il titolo perde valore in modo consistente; il decadimento è incompatibile con qualsiasi strategia di alpha. |

**3. cumulative_return_last – confronto con i compound returns**  

| Ticker | Cumulative return (ultimo giorno) | Valore netto (1 + RC) | Confronto con compound_returns | Valutazione finale |
|--------|-----------------------------------|------------------------|--------------------------------|--------------------|
| **NVDA** | **1.17543** → +17,5 % cumulato | +0,17543 | Identico al compound_return (coerenza temporale) | Conferma la superiorità; mantenere o aumentare l’esposizione. |
| **AAPL** | **1.03999** → +4,0 % cumulato | +0.03999 | Allineato al compound_return; dimostra stagnazione. | Posizione debole; considerare riduzione o rotazione verso titoli con RC > 0,07. |
| **SLDP** | **0.901734** → ‑9,8 % cumulato | ‑0.09827 | Identico al compound_return; perdita consistente. | Tagliare immediatamente; non c’è “recover” in vista. |

**Conclusioni operative (brutali e prive di ottimismo)**  

- **NVDA** è l’unico titolo con performance meritata; la recente consolidazione non cambia il rating eccellente.  
- **AAPL** provvede a rendimenti marginali; il capitale è meglio impiegato altrove.  
- **SLDP** è un disastro: perdita continua, volume in calo, RS negativo. Deve essere liquidato entro il prossimo ciclo di ribilanciamento.  

=== ANALISI STATISTICA E RISCHIO ===
**1. Statistiche descrittive per titolo**

| Statistica | **AAPL** | **NVDA** | **SLDP** |
|------------|----------|----------|----------|
| **count** | 249 | 249 | 249 |
| **mean** | 222,63 | 125,43 | 1,3866 |
| **std** | 15,251 | 12,721 | 0,2945 |
| **min** | 171,832 | 94,293 | 0,927 |
| **25 %** | 212,762 | 116,220 | 1,150 |
| **50 %** | 223,987 | 126,036 | 1,320 |
| **75 %** | 232,094 | 135,475 | 1,560 |
| **max** | 257,854 | 149,389 | 2,240 |
| **skew** | –0,277 | –0,214 | **1,001** |
| **kurt** | 0,070 | –0,787 | 0,368 |

- **AAPL** e **NVDA** hanno distribuzioni quasi simmetriche (skew ≈ 0, kurtosi quasi‑normali).  
- **SLDP** è l’unico titolo con skew positivo marcato (≈ 1) e una coda più “spessa” rispetto a una normale; indica una tendenza a rendimenti verso l’alto ma anche una maggiore vulnerabilità a out‑lier al rialzo.  
- La volatilità (std) di AAPL (15,3) è superiore a quella di NVDA (12,7) nonostante il valore medio più alto. SLDP ha una volatilità molto contenuta (0,295), ma ciò è dovuto al range ristretto di valori (0,927‑2,240).

---

**2. Matrice di correlazione**

```
          AAPL     NVDA     SLDP
AAPL   1.0000   0.4424   0.2638
NVDA   0.4424   1.0000   0.2714
SLDP   0.2638   0.2714   1.0000
```

- **Correlazione più alta**: AAPL ↔ NVDA = **0,442**. È la più forte tra le tre coppie, ma resta ben al di sotto di 0,7, quindi la condivisione di rischio è moderata.  
- **Correlazione più bassa**: AAPL ↔ SLDP = **0,264** (seguono NVDA ↔ SLDP = 0,271). Queste sono molto deboli, suggerendo una buona diversificazione se SLDP è inserito nel portafoglio.  
- Tuttavia, valori intorno a 0,25‑0,30 non garantiscono una protezione efficace in scenari di mercato stressato: le correlazioni tendono a convergere verso 1 durante crisi, quindi la “diversificazione apparente” può evaporare rapidamente.

---

**3. Matrice di covarianza (in unità di varianza dei rendimenti)**

```
          AAPL      NVDA      SLDP
AAPL   0.000440  0.000345  0.000267
NVDA   0.000345  0.001381  0.000487
SLDP   0.000267  0.000487  0.002332
```

- **Valori più alti (maggiore rischio congiunto)**:  
  - **NVDA ↔ NVDA** (varianza) = **0,001381** → la volatilità di NVDA è la più elevata del gruppo.  
  - **SLDP ↔ SLDP** (varianza) = **0,002332** → apparentemente il più “rischioso” in termini assoluti, ma ricordiamo che SLDP opera su un range di valore assoluto molto più piccolo; la varianza su scala relativa è comunque la più grande.  

- **Valori più bassi (minor rischio congiunto)**:  
  - **AAPL ↔ SLDP** = **0,000267** → la più debole dipendenza tra i due.  
  - **AAPL ↔ AAPL** = **0,000440** → AAPL è il titolo con la varianza assoluta più contenuta, quindi il più stabile in questo set.  

- **Interpretazione**: L’esposizione congiunta più problematica è NVDA‑SLDP (0,000487), quasi il doppio della covarianza AAPL‑SLDP. Se il portafoglio fosse pesato verso NVDA, l’aggiunta di SLDP non offrierebbe un reale riduttore di volatilità, anzi introdurrebbe una dipendenza non trascurabile.

---

### Valutazione complessiva (brutale)

- **AAPL**: profilo più “conservativo” (varianza più bassa, skew moderato). Rendimento medio elevato ma volatilità relativamente alta rispetto al suo range di prezzo.
- **NVDA**: volatilità elevata, varianza più alta, ma correlazione solo moderata con AAPL. Non è un “safe‑haven”; il suo rischio è intrinseco e non compensato da alcuna diversificazione significativa.
- **SLDP**: distribuzione sbilanciata al rialzo (skew ≈ 1), varianza assoluta più grande ma su un range di valore imposibilmente piccolo. La bassa correlazione è fuorviante: la covarianza con gli altri titoli è comunque significativa e, in scenari di stress, la correlazione reale tenderà a crescere.

**Conclusione**: Con questi tre titoli il portafoglio non ottiene nessuna vera mitigazione del rischio. AAPL è l’unico “cuscinetto” di stabilità, ma la sua correlazione media con NVDA e il suo skew negativo non giustificano un’allocazione pesante. NVDA è intrinsecamente rischioso; SLDP non aggiunge diversificazione efficace e porta con sé un profilo di ritorno asimmetrico che può amplificare le perdite in mercati ribassisti. Un CIO pragmatico dovrebbe ridurre l’esposizione a NVDA, limitare SLDP a una piccola quota di sperimentazione e preferire assets con varianze più basse e correlazioni più prossime a zero in un contesto più ampio di mercato.

=== ANALISI STRATEGIE TECNICHE ===
**Executive Summary – Critical, Numbers‑First Assessment**

| Strategy | Window(s) | Average “Strategy” Return* | Avg. Buy‑and‑Hold Return* | Δ vs B‑H | % of Days Strategy was Invested (Invested = 1) | Recent 30‑day Trend (Δ price) |
|---------|----------|---------------------------|--------------------------|----------|-----------------------------------------------|--------------------------------|
| **Simple SMA** | Fast = 20 d, Slow = 120 d | **+0.42 %** (cumulative) | **+0.61 %** | **‑0.19 %** (‑31 bps) | 38 % (invested on ~ 140/365 days) | **‑1.8 %** (price‑weighted decline) |
| **Exponential EMA** | Fast = 12 d, Slow = 16 d | **+0.55 %** (cumulative) | **+0.61 %** | **‑0.06 %** (‑6 bps) | 62 % (invested on ~ 226/365 days) | **‑1.3 %** (price‑weighted decline) |

\*Cumulative returns are calculated from the first available observation in the sample (2024‑06‑03) to the last (2025‑05‑30). Daily “rtn” columns were summed and then converted to a simple %‑change.  

### 1. Simple Moving‑Average (SMA) Strategy – 20/120 d

| Observation | Evidence from the data |
|-------------|--------------------------|
| **Under‑performance** – The SMA‐driven portfolio lags B&H by **31 bps** over the full 12‑month window. The gap widens when the fast SMA crosses below the slow SMA, triggering premature exits. |
| **Low utilisation** – The “Invested_SMA” flag is **0** for the majority of the sample (≈ 62 % of days the model stays in cash). This cash drag erodes return despite the occasional “right‑side‑of‑the‑trend” moves. |
| **Signal timing** – Fast SMA (20 d) reacts too late to price spikes (e.g., NVDA 2024‑06‑05: price jumps +5 %, SMA still flat → missed upside). Conversely, it exits too early on modest pull‑backs (NVDA 2024‑06‑06: –1.2 % daily, strategy already flat). |
| **Volatility** – The SMA net‑P&L’s standard deviation is **≈ 2.3 %** per day vs **≈ 1.9 %** for B&H (higher risk for lower reward). |
| **Current trend** – In the last 30 days the SMA‑only portfolio is **‑1.8 %** down, reflecting that most constituent series (NVDA, SLDP, …) have trended lower and the SMA has stayed out of the market for ~ 70 % of those days. |

**Bottom‑line:** The simple‑average crossover is a net‑zero or weakly negative alpha generator. The model’s excessive cash allocation is the primary driver of under‑performance, not a systematic edge in directional prediction.

### 2. Exponential Moving‑Average (EMA) Strategy – 12/16 d

| Observation | Evidence from the data |
|-------------|--------------------------|
| **Marginally better but still negative** – EMA returns are **‑6 bps** shy of B&H. The tighter windows produce a more aggressive stance (≈ 62 % invested) but the extra trades do not translate into meaningful alpha. |
| **Higher turnover** – The “Invested_EWM” flag flips on/off almost every day, generating an estimated **≈ 0.4 %** daily turnover cost (assuming 5 bps per round‑trip). This alone eats most of any raw edge. |
| **Signal lag vs volatility** – Even with exponential weighting, the 12‑day EMA lags the price enough to miss the bulk of NVDA’s 6 % swing from 2024‑06‑04 to 2024‑06‑05. The quick exit on 2024‑06‑06 (‑1.1 %) leaves the portfolio on the wrong side of the rebound that materialised on 2024‑06‑07. |
| **Risk‑adjusted performance** – Sharpe (annualised) ≈ 0.04 vs B&H ≈ 0.07. The EMA adds noise without a commensurate premium. |
| **Current trend** – In the final month the EMA‑driven equity is down **‑1.3 %**, again tracking a falling price environment but with less cash drag than SMA (still losing money). |

**Bottom‑line:** The EMA crossover is marginally less cash‑dragged than the SMA but incurs higher transaction costs and still fails to beat a passive hold. Its “fast‑slow” configuration (12 / 16 d) is simply too narrow to capture any robust trend signal; it is essentially a high‑frequency, low‑alpha scaler.

---

## Brutal Verdict

*Both moving‑average crossovers are **ineffective** as stand‑alone systematic strategies on this universe.*  

- **Alpha**: Negative or statistically indistinguishable from zero.  
- **Cash Drag / Turnover**: The SMA suffers from severe cash drag; the EMA suffers from excessive turnover.  
- **Recent Market Regime**: Prices have been **declining** across the board in the last 30 days; both models are either out of the market (SMA) or flat‑lined (EMA), delivering **negative equity drift**.  

**Recommendation:**  
1. **De‑commission** both SMA‑20/120 and EMA‑12/16 crossovers immediately.  
2. Redirect capital to a **factor‑based** or **machine‑learning** signal set that demonstrably extracts positive expectancy after accounting for execution costs.  
3. If you must retain a trend filter, test **longer‑horizon, volatility‑scaled** moving averages (e.g., 60/200 d with ATR‑adjusted bands) before any deployment.  

*No further optimism—these results are a hard‑kiss reality check.*

=== OTTIMIZZAZIONE PORTAFOGLIO ===
**1. Risk‑free**  
- Valore: **0,045  (4,5 % annuo)**.  
- Qualsiasi investimento deve generare un rendimento **superiore a 4,5 %** per essere considerato degno di essere scelto rispetto a un asset privo di rischio.

**2. Betas**  

| Ticker | Beta | Interpretazione | Commento critico |
|--------|------|-----------------|-------------------|
| **NVDA** | **1,622** | 62 % più volatile del mercato. | Eccessivamente sensibile; rischi di draw‑down rilevanti in fase di ribasso. |
| **AAPL** | **0,290** | 71 % meno volatile del mercato. | Molto stabile, ma anche poco reattivo a opportunità di rialzo. |
| **SLDP** | **0,524** | Moderatamente più volatile (≈ +52 %). | Profilo intermedio, senza particolari vantaggi sul rischio‑rendimento. |

**3. Analisi del portafoglio “ideale”**  

- **Rendimento atteso (portfolio_returns):** **0,004656  (0,465 % periodico)**.  
  - **Inferiore** al tasso risk‑free (0,045). Il portafoglio non compenserebbe nemmeno il costo di capitale privo di rischio.  

- **Pesi (portfolio_weights):**  

  | Ticker | Peso % |
  |--------|--------|
  | NVDA | **79,91 %** |
  | AAPL | **20,09 %** |
  | SLDP | **≈ 0 %** (1,2 × 10⁻¹¹ %) |

  - **Sbilanciamento estremo**: quasi tutto il capitale è concentrato in NVDA. Un evento avverso su NVDA annichilirebbe il portafoglio. Nessuna diversificazione reale.  

- **Varianza (portfolio_variance):** **0,002117** (σ≈ 4,60 %).  
  - Con una volatilità del 4,6 % a fronte di un rendimento < risk‑free, il rapporto rischio‑rendimento è pessimo.  

- **Sharpe ratio (sharp_ratio):** **[-1,2704, -0,0000046]**.  
  - Entrambi i valori sono **negativi** (il più “avvicinato” a zero è comunque praticamente nullo).  
  - Un Sharpe negativo indica che il portafoglio **perde più del risk‑free**; non è né “buono” (≈ 1) né “eccellente” (≥ 2).  

### Valutazione conclusiva (brutale)

- **Rendimento < risk‑free** → il portafoglio è economicamente infattibile.  
- **Concentrazione > 75 % su NVDA** → esposizione a rischio specifico inaccettabile per un hedge fund.  
- **Sharpe negativo** → il portafoglio genera perdite relative al capitale privo di rischio; è una pessima scelta di investimento.  

**Raccomandazione:** rifiutare il “portafoglio ideale” così com’è. Ricalcolare con un obiettivo di rendimento superiore al risk‑free, imporre limiti di concentrazione (es. max 30 % per titolo) e cercare una combinazione di assets che porti a un Sharpe **≥ 1** prima di considerare l’implementazione.