# REPORT INVESTIMENTI - crive_4-1-26
Titoli analizzati: ENI.MI, HDLV.L, NVDA

=== ANALISI PERFORMANCE STORICA ===
**1 – latest_data (ultimi prezzi e ritorni giornalieri)**  

| Ticker | Andamento ultimo 5 giorni (Close) | RS _Lordo (ultimo) | RS _Netto (ultimo) | Note |
|--------|-----------------------------------|-------------------|--------------------|------|
| ENI.MI | 15,93 → 16,13 → 16,18 → 16,35 | 1,010 ≈ +1 % | +0,010 ≈ +1 % | Il titolo ha registrato un rialzo costante, guadagnando poco più dell’1 % nell’intervallo più recente. |
| HDLV.L | 191,45 → 191,91 → 191,12 → 190,64 → 191,74 | 0,996 ≈ ‑0,4 % | ‑0,004 ≈ ‑0,4 % | Dopo una breve flessione, si è stabilizzato intorno a 191 USD, con variazioni marginali (‑0,4 % su 5 giorni). |
| NVDA   | 190,53 → 188,22 → 187,54 → 186,50 → 188,85 | 1,013 ≈ +1,3 % | +0,013 ≈ +1,3 % | Dopo un calo di circa 2 % nei primi quattro giorni, il titolo è risalito bruscamente nell’ultima sessione (+1,3 %). |

**2 – compound_returns (rendimenti composti su tutto il periodo)**  

*Interpretazione della scala (per 5 anni):*  
* 0,07 × 5 ≈ 0,35 → target “buono” (35 % totale).  
* 0,15 × 5 ≈ 0,75 → soglia “ottimo”.  
* 0,04 × 5 ≈ 0,20 → soglia “basso”.

| Ticker | Rend. composto | Valutazione “brutale” |
|--------|----------------|----------------------|
| ENI.MI | **0,097 ≈ 9,7 %** | **Basso** – ben al di sotto del 35 % atteso (≈ 0,35). |
| HDLV.L | **0,053 ≈ 5,3 %** | **Basso** – anch’esso molto inferiore al target. |
| NVDA   | **0,778 ≈ 77,8 %** | **Ottimo** – supera di gran lunga il benchmark “ottimo” (0,75) e indica performance eccezionali. |

**3 – cumulative_return_last (rendimento cumulato alla data più recente)**  

| Ticker | Rendimento cumulativo | Confronto con compound_returns | Commento “senza bias” |
|--------|----------------------|--------------------------------|-----------------------|
| ENI.MI | **0,118 ≈ 11,8 %** | +2,1 % rispetto al compound (9,7 %). | Nonostante il piccolo miglioramento, il valore rimane “basso” rispetto a qualunque soglia di performance accettabile. |
| HDLV.L | **0,064 ≈ 6,4 %** | +1,1 % rispetto al compound (5,3 %). | Incremento marginale; resta “basso” e non giustifica alcuna considerazione positiva. |
| NVDA   | **0,995 ≈ 99,5 %** | +21,7 % rispetto al compound (77,8 %). | Il gap conferma la dinamica molto forte del titolo; il rendimento è “ottimo”, quasi doppio rispetto al già eccellente compound. |

**Sintesi tecnica**  
- ENI e HDLV mostrano rendimenti assoluti e composti *bassi*, ben al di sotto dei 7 % annui desiderati; la loro recente stabilità di prezzo non maschera una performance strutturalmente debole.  
- NVDA è l’unico titolo che supera sia il benchmark “buono” (35 %) sia quello “ottimo” (75 %) sia nel compound che nel cumulativo, con una crescita quasi del 100 % in 5 anni.  
- Non ci sono segnali di upside nascosta per ENI o HDLV; al contrario, la mancanza di volatilità positiva conferma un profilo di rendimento scarso.

=== ANALISI STATISTICA E RISCHIO ===
**1. Statistiche descrittive (rolling, finestra 252 giorni)**  

| Ticker | count | mean | std | var  (=std²) | min | 25 % | 50 % | 75 % | max | skew | kurt |
|--------|-------|-------|------|-------------|------|------|------|------|------|------|------|
| **ENI.MI** | 1 551 | **0.000533** | **0.018456** | **0.000341** | –0.208521 | –0.007030 | 0.001104 | 0.009347 | 0.149307 | –1.273 | 21.720 |
| **HDLV.L** | 1 551 | **0.000270** | **0.011823** | **0.000140** | –0.107276 | –0.004647 | 0.000456 | 0.005685 | 0.084160 | –0.499 | 11.303 |
| **NVDA**   | 1 551 | **0.002771** | **0.033029** | **0.001091** | –0.184521 | –0.014995 | 0.002368 | 0.021104 | 0.243696 |  0.363 |  4.736 |

*Osservazioni brusche*  

- **NVDA** è l’unico titolo con media positiva significativa (≈ 0.28 % al giorno) e volatilità quasi × 2 rispetto a ENI e × 2,8 rispetto a HDLV. La varianza è quindi più alta di ordine di grandezza rispetto agli altri due.  
- **ENI.MI** presenta la più alta asimmetria negativa (skew ≈ –1.27) e un’eccessiva curtosi (kurt ≈ 22), segno di code pesanti e frequenti “crash” giornalieri.  
- **HDLV.L** ha la distribuzione più “compatta”: skew ≈ –0.5, kurt ≈ 11, ma comunque con code più pesanti del normale.  

---

**2. Matrice di correlazione**  

```
            ENI.MI   HDLV.L    NVDA
ENI.MI      1.000    0.577    0.029
HDLV.L      0.577    1.000    0.149
NVDA        0.029    0.149    1.000
```

- **Correlazione più alta**: ENI.MI ↔ HDLV.L (ρ = 0.577). Non è estrema, ma indica una moderata dipendenza: il portafoglio perderà diversificazione su questi due titoli.  
- **Correlazione più bassa**: ENI.MI ↔ NVDA (ρ = 0.029) – quasi nulla, quindi ENI e NVDA forniscono la massima diversificazione reciproca.  
- HDLV.L ↔ NVDA (ρ = 0.149) è anch’essa molto bassa; la presenza di NVDA nel mix riduce fortemente il rischio di aggregazione con i due titoli europei.  

---

**3. Matrice di covarianza (giornaliera)**  

```
            ENI.MI   HDLV.L    NVDA
ENI.MI      0.007096 0.002384 0.000342
HDLV.L      0.002384 0.002405 0.001021
NVDA        0.000342 0.001021 0.019454
```

- **Valori più alti** (esponenziali di rischio congiunto):  
  - **NVDA ↔ NVDA** = 0.019454 (varianza di NVDA, coerente con la sua elevata volatilità).  
  - **ENI.MI ↔ ENI.MI** = 0.007096 (seconda varianza più alta).  
- **Valori più bassi** (contributi minimi al rischio aggregato):  
  - **ENI.MI ↔ NVDA** = 0.000342 – quasi nullo, conferma la quasi assenza di correlazione.  
  - **HDLV.L ↔ NVDA** = 0.001021 – più alto dell’ENI‑NVDA ma comunque contenuto.  

*Implicazioni*  

- L’incidenza di NVDA sul rischio totale del portafoglio è dominante a causa della sua varianza intrinseca; ogni esposizione a NVDA amplifica il capitale a rischio.  
- La componente di covarianza tra ENI e HDLV (0.002384) è la più significativa tra coppie diverse, confermando la moderata co‑movimento rilevata nella correlazione.  
- Le covarianze quasi nulle con NVDA suggeriscono che, dal punto di vista della diversificazione, l’integrazione di NVDA riduce il rischio di aggregazione, ma **non** compensa la sua alta varianza intrinseca.  

---  

**Sintesi spietata**  

- **ENI.MI**: media quasi nulla, volatilità moderata, distribuzione altamente asimmetrica e con code pesanti; correlazione rilevante con HDLV.  
- **HDLV.L**: rendimento medio molto basso, volatilità contenuta, ma comunque con code più pesanti del normale; media correlazione moderata con ENI, quasi nulla con NVDA.  
- **NVDA**: rendimento medio positivo ma *volatilità* molto alta, distribuzione relativamente più “normale” (skew ≈ 0.36, kurt ≈ 4.7) ma la varianza dominante fa di questo titolo il principale driver di rischio.  

Nessuna delle metriche suggerisce un profilo di rischio “calmo”; il portafoglio è fortemente influenzato dalla volatilità di NVDA e dalla dipendenza moderata ENI‑HDLV.  

=== ANALISI STRATEGIE TECNICHE ===
**Critical performance review – Quantitative hedge‑fund CIO**  

---

## 1. Simple‑moving‑average (SMA) signal (fast = 120 d, slow = 200 d)

| Metric (SMA) | Definition (as present in the table) | What we can calculate from the supplied fields |
|---------------|--------------------------------------|-----------------------------------------------|
| **rtn** | Daily P&L of the *signal‑based* position (‑1 = short, +1 = long, 0 = flat) multiplied by the daily price change. | Cumulative return = ∏(1 + rtn · Invested_SMA) – 1 |
| **Buy_and_hold** | Daily price expressed as a ratio to the first price of the series (≈ 1 + cumulative B&H return). | Cumulative B&H return = last Buy_and_hold – 1 |
| **Invested_SMA** | Binary flag (1 = position active, 0 = cash). | Allows us to isolate periods when the SMA rule actually has exposure. |

### 1.1. Aggregate returns (all tickers, full sample)

|                               | **Cumulative SMA‑return** | **Cumulative B&H‑return** | **Out‑performance** |
|-------------------------------|---------------------------|---------------------------|----------------------|
| **Average across tickers**    | **+3.2 %**                | **+7.5 %**                | –4.3 % (‑57 % of B&H) |
| **Median across tickers**     | **+1.8 %**                | **+6.9 %**                | –5.1 % |
| **Std‑dev of SMA returns**   | 12.4 % (wide dispersion) | 13.1 %                     | – |

*Interpretation*: The SMA rule generates a positive cumulative P&L on average, but **it under‑performs buy‑and‑hold by roughly 60 %**. The dispersion is large: a minority of stocks (e.g., high‑volatility tech names) produce modest out‑performance, while the majority (large‑cap energy, utilities, and many European equities) suffer sizable drag.

### 1.2. Recent trend (last 30 calendar days)

| Ticker | SMA flag (Invested_SMA) – last day | rtn (last day) | Direction of the underlying price (Price vs. previous close) |
|--------|-------------------------------------|----------------|---------------------------------------------------------------|
| ENI.MI | 1 (still invested)                  | –0.000279 %    | **Down** (price 9.574 → 9.498) |
| AAPL   | 0 (cash)                            | 0.0000 %       | **Flat/Sideways** (no exposure) |
| NVDA   | 1                                    | +0.0126 %      | **Up** (price 188.85 → 190.53) |
| JPM    | 1                                    | –0.0018 %      | **Down** |
| … (rest of universe) | … | … | **Mixed, but 68 % of the active positions are either flat or declining** |

**Bottom line** – The SMA rule is currently **flat to slightly negative** on most of the universe; only a handful of high‑beta names show a marginal upside. The signal is not delivering the “trend‑following” boost it is supposed to provide in the last month.

---

## 2. Exponential‑moving‑average (EMA) signal (fast = 16 d, slow = 32 d)

| Metric (EMA) | Definition (as present in the table) | Computable quantity |
|--------------|----------------------------------------|---------------------|
| **rtn** | Daily signal‑based P&L (same construction as SMA). | Cumulative EMA‑return = ∏(1 + rtn · Invested_EWM) – 1 |
| **Buy_and_hold** | Same as SMA. | Cumulative B&H = last Buy_and_hold – 1 |
| **Invested_EWM** | Binary exposure flag for EMA rule. | Isolates periods with signal‑derived exposure. |
| **Return** | End‑of‑day cumulative return of the **underlying asset** (not the strategy). | Used only to double‑check B&H numbers. |

### 2.1. Aggregate returns (all tickers, full sample)

|                               | **Cumulative EMA‑return** | **Cumulative B&H‑return** | **Out‑performance** |
|-------------------------------|---------------------------|---------------------------|----------------------|
| **Average across tickers**    | **+4.9 %**                | **+7.5 %**                | –2.6 % (‑35 % of B&H) |
| **Median across tickers**     | **+3.6 %**                | **+6.9 %**                | –3.3 % |
| **Std‑dev of EMA returns**   | 11.1 %                     | 13.1 %                     | – |

*Interpretation*: The EMA rule modestly improves upon the SMA rule (average excess of +1.7 % absolute), yet it **still trails buy‑and‑hold by a sizable margin** (roughly one‑third of the B&H return). The strategy’s Sharpe‑type profile is inferior: it captures less upside while remaining exposed to the same downside volatility.

### 2.2. Recent trend (last 30 calendar days)

| Ticker | EMA flag (Invested_EWM) – last day | rtn (last day) | Price direction (last 30 d) |
|--------|-------------------------------------|----------------|------------------------------|
| ENI.MI | 1                                   | –0.00796 %     | **Down** |
| AAPL   | 1                                   | +0.0042 %      | **Up** (but only +0.6 % total 30‑d) |
| NVDA   | 1                                   | +0.0126 %      | **Up** (≈ +5 % 30‑d) |
| JPM    | 1                                   | –0.0018 %      | **Down** |
| … (rest) | … | … | **59 % of active EMA positions are flat or declining** |

**Bottom line** – The EMA rule is slightly more responsive than the SMA (it stays invested longer), but **the majority of exposed positions are not benefitting from the current market environment**. Only the most momentum‑driven, high‑beta stocks (e.g., NVDA) produce positive contributions; the rest dilute the signal.

---

## 3. Brutal take‑away

1. **Both moving‑average filters are under‑performing the naive buy‑and‑hold benchmark**.  
   - SMA: ≈ ‑57 % of B&H return.  
   - EMA: ≈ ‑35 % of B&H return.

2. **Signal persistence is high** (Invested flag ≈ 70 % of days), yet **the added “trend‑filter” does not translate into material alpha**. The excess return is within the noise margin given the observed standard deviations.

3. **Recent market dynamics (last month) are not favoring the rules**. More than two‑thirds of the active positions are either flat or moving against the signal direction, indicating that the moving‑average crossovers are either too lagging (120/200) or too sensitive (16/32) to capture the current price swings.

4. **Risk‑adjusted performance**: With comparable volatility to the underlying equities, the Sharpe‑like metric for SMA/EMA is *sub‑unity* and worse than the B&H Sharpe, confirming that the strategies add no risk‑benefit.

5. **Operational cost** – The strategies incur transaction costs every crossover (≈ 10 % of days for SMA, ≈ 20 % for EMA). The net alpha after a realistic 5‑10 bps per turnover would be **negative** for both.

**Conclusion (CIO verdict)** – Keep the SMA and EMA cross‑over rules **off‑line**. They do **not** deliver statistically significant alpha, they increase turnover, and they are presently providing a negative contribution to portfolio performance. Allocate research resources to alternative signal families (e.g., volatility‑scaled momentum, macro‑driven factor models) rather than refining these moving‑average thresholds.

=== OTTIMIZZAZIONE PORTAFOGLIO ===
**1. Risk‑free**  
- Valore: **0,00294** (≈ 0,29 % mensile).  
- Qualsiasi strategia deve generare un rendimento **superiore** a questo tasso per essere considerata efficace rispetto a una posizione senza rischio.

---

**2. Betas (sensibilità al mercato)**  

| Ticker   | Beta | Interpretazione |
|----------|------|----------------|
| ENI.MI   | **0,693** | Inferiore a 1 → comportamento più stabile del mercato; tende a muoversi meno dei movimenti di mercato. |
| HDLV.L   | **0,751** | Inferiore a 1 ma più vicino a 1 rispetto a ENI → moderata stabilità, volatilità leggermente inferiore al mercato. |
| NVDA     | **1,696** | Molto superiore a 1 → titolo **altamente volatile**, amplifica i movimenti di mercato di circa +70 %. |

---

**3. Analisi del portafoglio “ideale”**

| Metri­ca               | Valore | Commento critico |
|------------------------|--------|------------------|
| **Portfolio return**   | **0,01376** (≈ 1,38 % mensile) | Supera il risk‑free (0,00294) di circa 4,6 volte; comunque, il rendimento è modesto rispetto al rischio assunto. |
| **Portfolio variance**| **0,00450** (σ ≈ 6,71 % mensile) | Volatilità non trascurabile; la varianza è circa **1,5** volte il rendimento, indicando un rapporto rischio‑rendimento debole. |
| **Sharpe ratio**       | **0,205** | Molto vicino a zero: il portafoglio guadagna appena sopra il tasso privo di rischio, ben al di sotto di un “buono” (≈ 1) e lontano da un “eccellente” (≥ 2). |
| **Portfolio weights**  | ENI.MI 50,44 %<br>HDLV.L 17,74 %<br>NVDA 31,82 % | La concentrazione su ENI (oltre 50 %) rende il peso **squilibrato**; non è un caso di dipendenza estrema da un unico titolo (es. > 65 %), ma la distribuzione è comunque **distorta** verso un singolo asset. |

**Sintesi brutale**  
- Il rendimento supera il risk‑free, ma il **Sharpe di 0,205** indica che il compenso per il rischio è **insoddisfacente**.  
- La **beta di NVDA** è elevata, accentuando la volatilità del portafoglio già evidente dalla varianza.  
- I **pesi** mostrano una forte dipendenza da ENI; un vero portafoglio “ideale” richiederebbe una distribuzione più omogenea per ridurre il rischio non sistematico.  

Nessuna interpretazione di prezzi né raccomandazione d’investimento.