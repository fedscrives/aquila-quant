# REPORT INVESTIMENTI - gpt_20b_calcoli_precisi
Titoli analizzati: AMZN, MSFT, MU, PLTR, TSMC34.SA, 6033.KL

=== ANALISI PERFORMANCE STORICA ===
**1. Sintesi delle ultime quote (latest_datas)**  

| Ticker | Ultimo prezzo di chiusura | Trend a breve termine (5 d) | RS‑Lordo | RS‑Netto | RL | Commento tecnico |
|--------|---------------------------|-----------------------------|----------|----------|----|------------------|
| AMZN   | 232,38 | -0,3 % (chiusura 232 → 229) | 0,99 | –0,008 | –0,009 | Quasi‑equilibrio, lieve pressione di ribasso. |
| MSFT   | 349,73 | +0,2 % (chiusura 350 → 349) | 1,01 | +0,002 | +0,001 | Leggero rialzo, RS leggermente sopra 1. |
| MU     | 13,11 | +0,5 % (chiusura 13,10 → 13,12) | 1,00 | +0,000 | 0,000 | Perfetto equilibrio, nessuna spinta evidente. |
| PLTR   | 3,07 | –1,0 % (chiusura 3,08 → 3,07) | 0,99 | –0,004 | –0,005 | Pressione di ribasso moderata. |
| TSMC34.SA | 24,58 | +0,4 % (chiusura 24,60 → 24,58) | 1,01 | +0,002 | +0,001 | Leggero rialzo, RS > 1. |
| 6033.KL | 18,18 | +0,3 % (chiusura 18,14 → 18,18) | 1,00 | +0,000 | 0,000 | Equilibrato, nessuna pressione. |

*Nota*: i valori di RS (RS_Lordo e RS_Netto) oscillano intorno a 1, quindi non evidenziano over‑bought o over‑sold. RL rimane vicino a 0, quindi i segnali di trading sono deboli.

---

**2. Analisi dei rendimenti composti (compound_returns)**  

- **6033.KL**: 0,0628 → **moderatamente buono** (vicino a 0,07/anno).  
- **AMZN, MSFT, MU, PLTR, TSMC34.SA**: **NaN** → **inconcludibile**; non possiamo giudicare senza dato.

*Interpretazione*: per 6033.KL il rendimento annuo composto è leggermente inferiore al target di 0,07; non c’è alcuna indicazione di performance “ottima” ( > 0,15) o “bassa” (< 0,04). Gli altri titoli, con valori non disponibili, rimangono totalmente in valutazione.

---

**3. Rendimento cumulativo a 5 anni (cumulative_return_last)**  

| Ticker | Cumulative Return (5 anni) | Commento brutale |
|--------|---------------------------|-------------------|
| 6033.KL | 0,0686 | ~6,9 % su 5 anni → in linea con il compound, quindi **mediamente accettabile**. |
| AMZN | 0,0816 | 8,2 % → leggermente **oltre** 0,07, ma la mancanza di compound rende la comparazione inutile. |
| MSFT | 0,1863 | 18,6 % → **eccellente** se considerato su 5 anni, ma senza dato di compound non è chiaro se la crescita sia sostenibile. |
| MU | 0,4678 | 46,8 % → **estremamente forte** a 5 anni; se fosse composto sarebbe sopra 0,15/anno, ma il dato manca. |
| PLTR | 0,7889 | 78,9 % → **sorprendentemente alto**; senza compound non possiamo valutare la consistenza. |
| TSMC34.SA | 0,3319 | 33,2 % → **buono** a 5 anni; ma, come per gli altri, la comparazione con compound è impossibile. |

**Conclusione**: la curva cumulativa indica che, a 5 anni, tutti i titoli (tranne 6033.KL) hanno superato il benchmark di 0,07/anno. Tuttavia, la mancanza di dati di compound per la maggior parte dei titoli limita seriamente l’analisi comparativa. Solo per 6033.KL possiamo dire che la performance annua composta è in linea con il ritorno cumulativo. Per gli altri, la valutazione rimane aperta e non può essere supportata da metriche coerenti.

=== ANALISI STATISTICA E RISCHIO ===
**1. Statistiche descrittive per ticker**

| Ticker    | count | mean     | std       | min       | 25%      | 50%      | 75%      | max      | skew   | kurt   |
|-----------|-------|----------|-----------|-----------|----------|----------|----------|----------|--------|--------|
| 6033.KL   | 1367  | 0.000289 | 0.009638  | -0.044318 | -0.00379 | 0.000000 | 0.004469 | 0.086124 | 0.8068 | 7.7261 |
| AMZN      | 1367  | 0.000522 | 0.021687  | -0.140494 | -0.01066 | 0.000000 | 0.012066 | 0.135359 | 0.1475 | 5.3013 |
| MSFT      | 1367  | 0.000752 | 0.015941  | -0.077156 | -0.00714 | 0.000159 | 0.009662 | 0.101337 | 0.1934 | 3.3280 |
| MU        | 1367  | 0.001847 | 0.029774  | -0.161790 | -0.01381 | 0.000141 | 0.017402 | 0.188129 | 0.1177 | 3.6963 |
| PLTR      | 1367  | 0.003065 | 0.043863  | -0.213080 | -0.01950 | 0.000000 | 0.021791 | 0.308014 | 1.0656 | 6.3742 |
| TSMC34.SA | 1367  | 0.001329 | 0.023765  | -0.142525 | -0.01185 | 0.000000 | 0.012754 | 0.162277 | 0.6095 | 4.5047 |

**2. Matrice di correlazione**

| Ticker | 6033.KL | AMZN  | MSFT | MU   | PLTR | TSMC34.SA |
|--------|---------|-------|------|------|------|-----------|
| 6033.KL| 1.0000  | 0.0755| 0.132| 0.192| 0.333| -0.0531   |
| AMZN   | 0.0755  | 1.0000| 0.630| 0.388| 0.375| 0.4297    |
| MSFT   | 0.1320  | 0.6300| 1.000| 0.307| 0.320| 0.4988    |
| MU     | 0.1918  | 0.3875| 0.307| 1.000| 0.173| 0.4178    |
| PLTR   | 0.3335  | 0.3747| 0.319| 0.173| 1.000| 0.2782    |
| TSMC34.SA | -0.0531| 0.4297| 0.4988| 0.4178| 0.2782| 1.0000   |

- **Massima correlazione**: AMZN–MSFT = **0.6300** (alto rischio di non diversificazione).
- **Minima correlazione**: 6033.KL–TSMC34.SA = **‑0.0531** (minima diversificazione, ma molto debole).

**3. Matrice di covarianza**

| Ticker | 6033.KL | AMZN  | MSFT | MU   | PLTR | TSMC34.SA |
|--------|---------|-------|------|------|------|-----------|
| 6033.KL| 0.001292| 0.000236| 0.000300| 0.000919| 0.003566| -0.000189 |
| AMZN   | 0.000236| 0.007549| 0.003460| 0.004491| 0.009683| 0.003706  |
| MSFT   | 0.000300| 0.003460| 0.003996| 0.002587| 0.006012| 0.003130  |
| MU     | 0.000919| 0.004491| 0.002587| 0.017790| 0.006872| 0.005532  |
| PLTR   | 0.003566| 0.009683| 0.006012| 0.006872| 0.088464| 0.008215  |
| TSMC34.SA| -0.000189| 0.003706| 0.003130| 0.005532| 0.008215| 0.009854  |

- **Massimo valore di covarianza**: PLTR–PLTR (varianza) = **0.088464** → rischio interno molto elevato.
- **Minimo valore di covarianza**: 6033.KL–TSMC34.SA = **‑0.000189** → rischio minimo tra questi due.
- Le covarianze positive più elevate sono tra PLTR e AMZN (0.009683) e PLTR e MSFT (0.006012).

=== ANALISI STRATEGIE TECNICHE ===
**1. Medie mobili semplici (SMA 120 vs 200)**  

| KPI | SMA‑120 | SMA‑200 | Buy‑and‑Hold |
|-----|---------|---------|--------------|
| **Media giornaliera di ritorno** | +0.00012 | +0.00010 | +0.00018 |
| **Ritorno cumulativo (2020‑01‑02 → 2026‑01‑06)** | +0.45 % | +0.40 % | +0.78 % |
| **Sharpe (σ = 0.0045)** | 0.026 | 0.022 | 0.040 |

- La strategia SMA‑120 ha prodotto un ritorno cumulativo del 0,45 % in un periodo di 6 anni, il 41 % in meno del buy‑and‑hold.  
- La differenza media di ritorno giornaliero è di soli 0,00006 punti rispetto all’asset‑baseline; in pratica, la strategia aggiunge circa 0,02 punto di ritorno al giorno.  
- La volatilità del portafoglio SMA‑120 è inferiore di circa il 5 % rispetto al buy‑and‑hold, ma il rendimento più basso non giustifica l’esposizione ridotta.

**Trend nell’ultimo periodo (2025‑12‑01 → 2026‑01‑06)**  

- **Ritardo positivo/negativo**: tutti i ticker mostrano una media di ritorno giornaliero negativa (‑0,0010 ≈ ‑0,1 %) rispetto alla baseline positiva (≈ +0,19 %).  
- Il trend di prezzo è in ribasso: i prezzi di chiusura hanno avuto una diminuzione media del 0,3 % negli ultimi 30 giorni.  
- La strategia SMA, basata su segnali di crossover, continua a produrre posizioni di vendita in questo regime di trend ribassista, quindi non aggiunge valore addizionale.

---

**2. Medie mobili esponenziali (EMA 16 vs 32)**  

| KPI | EMA‑16 | EMA‑32 | Buy‑and‑Hold |
|-----|--------|--------|--------------|
| **Media giornaliera di ritorno** | +0.00014 | +0.00013 | +0.00018 |
| **Ritorno cumulativo (2020‑02‑03 → 2026‑01‑06)** | +0.60 % | +0.55 % | +0.78 % |
| **Sharpe (σ = 0.0042)** | 0.033 | 0.031 | 0.040 |

- La strategia EMA‑16 supera leggermente EMA‑32 di 0,05 % cumulativo, ma resta ancora un 23 % in meno del buy‑and‑hold.  
- La differenza media di ritorno giornaliero è di 0,00004 rispetto all’asset‑baseline; il valore incrementale è estremamente marginale.  
- La volatilità di EMA‑16 è circa il 3 % inferiore a quella del buy‑and‑hold, ma la performance globale resta significativamente più debole.

**Trend nell’ultimo periodo (2025‑12‑01 → 2026‑01‑06)**  

- **Ritardo positivo/negativo**: i ritorni giornalieri medi dei ticker EMA sono negativi (≈ ‑0,0010 %) mentre la baseline resta positiva (+ 0,19 %).  
- Il trend di prezzo è ribassista: le chiusure di fine dicembre sono state in media –0,3 % rispetto a fine novembre.  
- La logica di crossover EMA, in presenza di un trend ribassista, tende a generare segnali di uscita in anticipo, ma non a ritardare l’esposizione al ribasso, quindi non aggiunge valore aggiuntivo.

---

### Valutazione finale

- **SMA**: performance cumulativa 0,45–0,40 % contro 0,78 % buy‑and‑hold → sotto‑performanza del 42–46 %.  
- **EMA**: performance cumulativa 0,55–0,60 % contro 0,78 % buy‑and‑hold → sotto‑performanza del 27–32 %.  
- In entrambi i casi, la differenza media di ritorno giornaliero è inferiore a 0,00007, cioè 0,007 % di incremento, che non giustifica la riduzione dell’esposizione.  
- L’ultimo periodo mostra chiaramente una fase ribassista per i ticker e un ritorno negativo per le strategie di crossover, dimostrando che la loro capacità di catturare momentum positivo è debole.

**Conclusione**: Le strategie di medie mobili semplici ed esponenziali, come impostate (120/200 e 16/32), forniscono rendimenti significativamente inferiori a quelli di una posizione buy‑and‑hold e mostrano un trend negativo nell’ultimo periodo. Non vi è alcun indicatore di valore aggiunto; le strategie dovrebbero essere riconsiderate o abbandonate se l’obiettivo è massimizzare il ritorno netto.

=== OTTIMIZZAZIONE PORTAFOGLIO ===
**Valutazione tecnica del portfolio ottimale**

| Variabile | Valore | Commento tecnico |
|-----------|--------|------------------|
| **risk_free** | 0.00294 (≈ 0.294 % mensile) | Ogni investimento deve superare questo benchmark; altrimenti il portafoglio è “in default” rispetto al tasso privo di rischio. |
| **betas** | <br>AMZN = 1.2928 <br>MSFT = 1.0335 <br>MU = 1.5642 <br>PLTR = 2.6156 <br>TSMC34.SA = 0.9132 <br>6033.KL = 0.2691 | *Beta > 1* indica maggiore volatilità rispetto al mercato; AMZN, MU e PLTR sono tutti “high‑beta” (PLTR estremamente volatile). <br>*Beta < 1* indica stabilità; 6033.KL è quasi “tangentiale” al mercato, TSMC34.SA leggermente sotto. |
| **portfolio_returns** | 0.01443 (≈ 1.44 % mensile) | **> risk_free**; la differenza di circa 0.0115 (≈ 1.15 %) è la premia di rischio mensile realizzata. |
| **portfolio_variance** | 0.00310 | Std. dev. mensile ≈ 5.57 %. |
| **portfolio_weights** | 25 % AMZN, 8.46 % MSFT, 25 % MU, 15.54 % PLTR, 1 % TSMC34.SA, 25 % 6033.KL | **Non equilibrato**: quattro titoli ricevono 25 % ciascuno; l’esposizione è concentrata e non si avverte di un “bunching” eccessivo, ma la diversificazione è ridotta rispetto a una allocazione 6‑titoli più uniforme. |
| **sharpe_ratio_mensile** | 0.259 | Rendimento per unità di rischio mensile moderato. |
| **sharpe_ratio_annuale** | 0.897 (scalato *√12*) | Classificato come **accettabile** (0.5 – 1.0). Non è un “buono” (≥ 1.0) né “eccellente” (> 1.5). |

**Sintesi critico**

* Il portafoglio supera il tasso privo di rischio, ma solo di una margine di ~1 % mensile.  
* La composizione è fortemente influenzata da quattro titoli al 25 % ciascuno, con un’assenza di asset a basso beta (es. 6033.KL è il più stabile).  
* La varianza mensile è relativamente contenuta, ma la correlazione tra i titoli (non mostrata) potrebbe aumentare la volatilità.  
* Sharpe annuale “accettabile” indica che la remunerazione per rischio non è competitiva rispetto ad altri portafogli più aggressivi o diversificati.  

Il risultato finale è un portfolio che, sebbene tecnicamente “ottimale” secondo il modello, offre un payoff di rischio‑premia moderato e una diversificazione insufficiente per l’orizzonte mensile.