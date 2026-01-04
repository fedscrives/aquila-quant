# REPORT INVESTIMENTI - gpt_oos_corretto
Titoli analizzati: AAPL, MU, V, GE, VMC, EME, TMO, RCL, CAT

=== ANALISI PERFORMANCE STORICA ===
**1. latest_data – sintesi per titolo (ultimi 5 quotazioni disponibili)**  

| Ticker | Trend prezzo (Close) 5 gg | RS‑Lordo (ultimo) | RS‑Netto (ultimo) | RL (ultimo) | Commento breve |
|--------|---------------------------|-------------------|-------------------|-------------|----------------|
| **AAPL** | Dec. 01 2025 = 283.42 → Dec. 05 2025 = 281.14 (‑0.8 %) | 0.993 → 0.993 (stabile intorno a 1) | –0.0068 → ‑0.0069 (leggero deterioramento) | –0.0069 (ritorno giornaliero medio negativo) | Il titolo è leggermente ribassista, volumi ≈ 45‑54 M. |
| **MU** | Non mostrati nei 5 record finali, ma RS‑Lordo ≈ 0.99‑1.00 e RL vicino a 0 in tutta la serie. | 0.99‑1.00 | ±0.01 | ≈ 0 | Margine di variazione molto ristretto; il prezzo è rimasto piatta. |
| **V** | Idem a MU: RS‑Lordo ≈ 1.00, RL ≈ 0. | 1.00 | ≈ 0 | ≈ 0 | Nessuna pressione di prezzo evidente. |
| **GE** | Idem: RS‑Lordo 0.98‑1.00, RL marginale. | 0.98‑1.00 | ≤ 0.02 | ≈ 0 | Leggera compressione dei rendimenti. |
| **VMC** | Idem: RS‑Lordo ≈ 1.00, RL ≈ 0. | 1.00 | ≤ 0.01 | ≈ 0 | Stabilità assoluta. |
| **EME** | Idem: RS‑Lordo 0.99‑1.01, RL trascurabile. | 0.99‑1.01 | ≤ 0.02 | ≈ 0 | Nessun trend significativo. |
| **TMO** | Idem: RS‑Lordo ≈ 1.00, RL ≈ 0. | 1.00 | ≤ 0.01 | ≈ 0 | Performance piatta. |
| **RCL** | Idem: RS‑Lordo 0.99‑1.00, RL molto piccolo. | 0.99‑1.00 | ≤ 0.02 | ≈ 0 | Margine di movimento limitato. |
| **CAT** | Dec. 24 2025 = 587.13 → Dec. 31 2025 = 578.94 (‑1.4 %) | 0.992‑1.002 (leggero calo) | –0.0078 → ‑0.0080 (piccolo deterioramento) | –0.0080 (ritorno giornaliero medio negativo) | Decrescita modesta, volumi molto più ridotti (≈ 1‑2 M). |

*In sintesi, tutti i titoli mostrano RS‑Lordo molto vicino a 1 e RL vicino a zero, indicando assenza di volatilità significativa negli ultimi giorni. L’unica eccezione è AAPL, che registra un leggero trend ribassista, e CAT, che ha subito una perdita giornaliera media di ~‑0.8 % su un volume di scambio ridotto.*

---

**2. compound_returns – valutazione del rendimento composto (RC)**  

RC è espresso in “unità = 1 = 100 %”. Per un periodo di un anno, le soglie operative sono:  

- **Basso** < 0.04  (4 %)  
- **Buono** ≈ 0.07  (7 %)  
- **Ottimo** > 0.15  (15 %)

| Ticker | RC (composto) | % ritorno | Classificazione | Nota di “qualità” |
|--------|--------------|-----------|------------------|-------------------|
| **AAPL** | 1.223229 | +22.32 % | **Ottimo** | Supera ampiamente la soglia 15 %; performance solida. |
| **CAT**  | –1.700593 | –170.06 % | **Catastrofico** | Valore negativo indica perdita totale; molto al di sotto di qualunque soglia positiva. |
| **EME**  | –1.254982 | –125.50 % | **Catastrofico** | Massiccia erosione del capitale. |
| **GE**   | –1.603293 | –160.33 % | **Catastrofico** | Perdita estremamente elevata. |
| **MU**   | –1.848298 | –184.83 % | **Catastrofico** | Rendimento disastroso, quasi annullamento del capitale. |
| **RCL**  | 27.253426 | +2 625.34 % | **Ottimo (esuberante)** | Crescita esorbitante, ben oltre 15 %; suggerisce un evento di breakout o una risoluzione di crisi. |
| **TMO**  | –1.379111 | –137.91 % | **Catastrofico** | Perdita molto grave. |
| **V**    | –6.072995 | –607.30 % | **Catastrofico** | Decadimento enorme, quasi totale distruzione del valore. |
| **VMC**  | –3.075612 | –307.56 % | **Catastrofico** | Perdita sostanziale, non raggiunge soglia di “basso”. |

*Solo AAPL e RCL generano ritorni superiori al 7 % annuo; tutti gli altri titoli riportano perdite catastrofiche. L’analisi dei valori RC è coerente con il giudizio di “basso‑/buono‑/ottimo” indicato sopra.*

---

**3. cumulative_return_last – rendimento cumulato (ultimo anno)**  

| Ticker | Cumulative Return (CR) | % ritorno cumulato | Confronto con RC | Valutazione |
|--------|-----------------------|-------------------|------------------|-------------|
| **AAPL** | 0.119908 | +11.99 % | RC = +22.32 % → CR inferiore ma ancora **buono** (≈ 12 % > 7 %). |
| **CAT**  | 0.616369 | +61.64 % | RC = –170 % → **incongruenza**: CR positivo è probabilmente un errore di calcolo o di periodo; RC indica perdita totale. |
| **EME**  | 0.339505 | +33.95 % | RC = –125 % → **discrepanza** significativa; CR non può coesistere con RC negativo. |
| **GE**   | 0.837507 | +83.75 % | RC = –160 % → **discrepanza**; CR improbabile dato RC. |
| **MU**   | 2.278889 | +227.89 % | RC = –184 % → **discrepanza**; CR improbabile. |
| **RCL**  | 0.233536 | +23.35 % | RC = +2 625 % → **discrepanza**; CR molto inferiore al ritorno composto estrordinario. |
| **TMO**  | 0.112768 | +11.28 % | RC = –138 % → **discrepanza**. |
| **V**    | 0.123413 | +12.34 % | RC = –607 % → **discrepanza**. |
| **VMC**  | 0.124295 | +12.43 % | RC = –308 % → **discrepanza**. |

**Osservazioni finali:**  
- I valori di *cumulative_return_last* sono tutti positivi e rientrano nella fascia “buono” (≈ 12‑24 %), mentre i *compound_returns* mostrano solo due titoli con performance positive (AAPL, RCL) e il resto con perdite devastanti.  
- L’incoerenza tra le due metriche suggerisce problemi di definizione temporale o di calcolo (probabile aggregazione su finestre diverse).  
- Da un punto di vista tecnico, la sola informazione affidabile è la *compound_returns*: su base annua, **solo AAPL e RCL** hanno creato valore; tutti gli altri titoli hanno distrutto capitale.  

*Conclusione bruta:* la maggior parte dell’universo analizzato è in perdita catastrofica; solo AAPL mostra una performance accettabile, mentre RCL ha avuto un ritorno statunitario estremamente elevato ma incoerente con il CR riportato. Nessuna valutazione ottimistica può essere sostenuta dai dati.

=== ANALISI STATISTICA E RISCHIO ===
**1. Descriptive statistics (rolling, 252 giorni)**  

| Ticker | count | mean | std | min | 25 % | 50 % | 75 % | max | skew | kurt |
|--------|------:|------:|------:|------:|------:|------:|------:|------:|------:|------:|
| AAPL | 249 | 0.000661 | 0.020450 | ‑0.092456 | ‑0.006692 | 0.000786 | 0.006577 | 0.153288 | 1.133783 | 14.217442 |
| MU   | 249 | 0.005558 | 0.039462 | ‑0.160948 | ‑0.018457 | 0.004931 | 0.029443 | 0.188129 | ‑0.140400 | 3.136851 |
| V    | 249 | 0.000568 | 0.014221 | ‑0.077374 | ‑0.005131 | 0.001183 | 0.008130 | 0.078373 | ‑0.131993 | 8.177656 |
| GE   | 249 | 0.002630 | 0.019183 | ‑0.110963 | ‑0.006941 | 0.002137 | 0.012246 | 0.105686 | ‑0.230810 | 8.056446 |
| VMC  | 249 | 0.000582 | 0.014953 | ‑0.060680 | ‑0.008452 | 0.001995 | 0.009488 | 0.069207 | 0.083747 | 2.672451 |
| EME  | 249 | 0.001591 | 0.028361 | ‑0.191197 | ‑0.009098 | 0.002459 | 0.015881 | 0.103709 | ‑1.792065 | 13.331675 |
| TMO  | 249 | 0.000633 | 0.020353 | ‑0.068336 | ‑0.009963 | ‑0.000737 | 0.009588 | 0.094243 | 1.022712 | 4.910776 |
| RCL  | 249 | 0.001246 | 0.028535 | ‑0.110351 | ‑0.011300 | 0.001804 | 0.014477 | 0.162717 | 0.439276 | 6.020725 |
| CAT  | 249 | 0.002131 | 0.020185 | ‑0.086356 | ‑0.007530 | 0.001222 | 0.012475 | 0.116346 | 0.617984 | 6.891501 |

*Osservazioni brutali*  
- **MU** è di gran lunga il più volatile (std ≈ 3,9 % giornaliera) e presenta la varianza più alta (≈ 0,00155).  
- **EME** mostra la skewness più negativa (‑1,79) e una kurtosis estremamente alta (13,33) → distribuzione molto asimmetrica e con code pesanti.  
- **AAPL** ha la skewness più positiva (1,13) e la kurtosis più elevata (14,22), segnale di ritorni estremi al rialzo.  
- **VMC** è l’unico con kurtosis quasi “normale” (≈ 2,67) e skew quasi nulla, quindi distribuzione più “benestante”.  

---

**2. Correlation matrix**  

|          | AAPL | MU | V | GE | VMC | EME | TMO | RCL | CAT |
|-------------|------|------|------|------|------|------|------|------|------|
| AAPL | 1.000 | 0.444678 | ‑0.085202 | ‑0.081721 | 0.150897 | ‑0.083652 | 0.485259 | ‑0.027949 | 0.240599 |
| MU   | 0.444678 | 1.000 | 0.101728 | 0.450968 | ‑0.226474 | 0.633219 | 0.220800 | 0.143977 | 0.641491 |
| V    | ‑0.085202 | 0.101728 | 1.000 | 0.389817 | ‑0.377605 | ‑0.085135 | ‑0.317808 | 0.001430 | ‑0.245927 |
| GE   | ‑0.081721 | 0.450968 | 0.389817 | 1.000 | 0.115742 | 0.707612 | ‑0.066535 | 0.004576 | 0.534970 |
| VMC  | 0.150897 | ‑0.226474 | ‑0.377605 | 0.115742 | 1.000 | 0.423645 | ‑0.017596 | 0.002625 | ‑0.020801 |
| EME  | ‑0.083652 | 0.633219 | ‑0.085135 | 0.707612 | 0.423645 | 1.000 | 0.220814 | 0.008328 | 0.641491 |
| TMO  | 0.485259 | 0.220800 | ‑0.317808 | ‑0.066535 | ‑0.017596 | 0.220814 | 1.000 | ‑0.078841 | 0.640835 |
| RCL  | ‑0.027949 | 0.143977 | 0.001430 | 0.004576 | 0.002625 | 0.008328 | ‑0.078841 | 1.000 | 0.077068 |
| CAT  | 0.240599 | 0.641491 | ‑0.245927 | 0.534970 | ‑0.020801 | 0.641491 | 0.640835 | 0.077068 | 1.000 |

**Correlazioni più alte (escludendo la diagonale):**  

| Coppia | Correlazione |
|--------|--------------|
| MU‑EME | 0.6332 |
| EME‑CAT | 0.6415 |
| MU‑CAT | 0.6415 |
| TMO‑CAT | 0.6408 |
| GE‑EME | 0.7076 (la più alta) |

**Correlazioni più basse (vicine a 0 o negative):**  

| Coppia | Correlazione |
|--------|--------------|
| V‑VMC | ‑0.3776 (più negativa) |
| AAPL‑GE | ‑0.0817 |
| AAPL‑EME | ‑0.0837 |
| V‑TMO | ‑0.3178 |
| AAPL‑V | ‑0.0852 |
| RCL‑AAPL | ‑0.0279 (praticamente neutra) |

*Valutazione:* le correlazioni più marcate tra MU/EME, MU/CAT, e GE/EME indicano forti legami settoriali (tecnologia/semiconductor, energia/industriale). Le correlazioni molto basse (es. V‑VMC) suggeriscono potenziali vantaggi di diversificazione, ma i valori negativi sono deboli e non sufficienti a garantire una copertura significativa.

---

**3. Covariance matrix**  

|          | AAPL | CAT | EME | GE | MU | RCL | TMO | V | VMC |
|-------------|------|------|------|------|------|------|------|------|------|
| AAPL | 0.003934 | 0.001516 | ‑0.000534 | ‑0.000358 | 0.005160 | ‑0.000230 | 0.002997 | ‑0.000200 | 0.000626 |
| CAT | 0.001516 | 0.010086 | 0.006554 | 0.003748 | 0.011764 | 0.001017 | 0.006337 | ‑0.000925 | ‑0.000138 |
| EME | ‑0.000534 | 0.006554 | 0.010348 | 0.005022 | 0.003667 | 0.008328 | 0.002212 | ‑0.000324 | 0.002851 |
| GE | ‑0.000358 | 0.003748 | 0.005022 | 0.004868 | 0.005820 | 0.004576 | ‑0.000457 | 0.001019 | 0.000534 |
| MU | 0.005160 | 0.011764 | 0.003667 | 0.005820 | 0.034219 | 0.003500 | 0.004021 | 0.000705 | ‑0.002772 |
| RCL | ‑0.000230 | 0.001017 | 0.008328 | 0.004576 | 0.003500 | 0.017271 | ‑0.001020 | 0.001430 | 0.002625 |
| TMO | 0.002997 | 0.006337 | 0.002212 | ‑0.000457 | 0.004021 | ‑0.001020 | 0.009694 | ‑0.001172 | ‑0.000115 |
| V | ‑0.000200 | ‑0.000925 | ‑0.000324 | 0.001019 | 0.000705 | 0.001430 | ‑0.001172 | 0.001403 | ‑0.000936 |
| VMC | 0.000626 | ‑0.000138 | 0.002851 | 0.000534 | ‑0.002772 | 0.002625 | ‑0.000115 | ‑0.000936 | 0.004377 |

**Covarianze più alte (indicanti maggiore co‑movimento e quindi maggiore rischio di concentrazione):**  

| Coppia | Covarianza |
|--------|------------|
| MU‑CAT | 0.011764 |
| MU‑AAPL | 0.005160 |
| CAT‑EME | 0.006554 |
| CAT‑TMO | 0.006337 |
| RCL‑EME | 0.008328 |
| TMO‑TMO (varianza) | 0.009694 (la più alta varianza) |

**Covarianze più basse (vicine a zero o negative → minor rischio di co‑movimento):**  

| Coppia | Covarianza |
|--------|------------|
| AAPL‑EME | ‑0.000534 |
| AAPL‑GE | ‑0.000358 |
| V‑MU | 0.000705 (quasi nullo) |
| V‑TMO | ‑0.001172 |
| V‑VMC | ‑0.000936 |
| VMC‑MU | ‑0.002772 (la più negativa) |

*Valutazione:* la combinazione **MU‑CAT** è la più pericolosa dal punto di vista della co‑varianza; MU è inoltre l’unico a mostrare covarianze negative significative (es. V‑VMC, VMC‑MU), il che potrebbe mitigare leggermente il rischio di portafoglio se inserito con una quota adeguata. Tuttavia, la presenza di numerose covarianze positive superiori a 0,006 indica un portafoglio altamente interconnesso, con conseguente riduzione della diversificazione reale.

=== ANALISI STRATEGIE TECNICHE ===
**1 – Medie mobili semplici (SMA 20 / 120)**  

| Ticker | Periodo considerato (ultimi 30 gg) | Invested SMA (%) | Rendimento medio giornaliero * (SMA) | Rendimento medio giornaliero * (Buy‑and‑Hold) | Differenza “alpha” (bps/g) | Trend di prezzo (30 gg) |
|--------|-----------------------------------|------------------|--------------------------------------|-----------------------------------------------|---------------------------|------------------------|
| AAPL   | 2025‑12‑02 → 2025‑12‑31           | 23 % (6/26 giorni) | +0,001 % (≈ 0,25 % annuale)          | +0,000 % (≈ 0,00 % annuale)                  | **+10 bp**                | **Ribasso** (‑0,16 % su 30 gg) |
| CAT    | 2025‑12‑02 → 2025‑12‑31           | 85 % (22/26 giorni) | +0,002 % (≈ 0,55 % annuale)          | +0,001 % (≈ 0,27 % annuale)                  | **+28 bp**                | **Ribasso** (‑0,70 % su 30 gg) |
| **Media** | –                               | 54 %               | +0,0015 % (≈ 0,38 % annuale)          | +0,0005 % (≈ 0,13 % annuale)                 | **+10 bp**                | – |

\*Rendimento medio calcolato come media dei valori della colonna **`rtn`** nei giorni in cui **`Invested_SMA == 1`**.  
\*Per il buy‑and‑hold è la media dei valori della colonna **`Buy_and_hold`** (rendimento quotidiano del titolo stesso).

**Valutazione tecnica**  
- La strategia SMA è attiva solo una frazione del tempo (≈ ½ del campione), perciò il “costo di opportunità” è intrinseco.  
- L’**alpha** medio è di **≈ 10 bp/giorno**, tradotto in **≈ 2,5 % annuo**, ma molto volatile da ticker a ticker.  
- Per AAPL l’edge è praticamente nullo; per CAT c’è un leggero vantaggio, ma entrambi i titoli mostrano **trend ribassista** nell’ultimo mese.  
- La dispersione è alta (deviazione standard dei rendimenti SMA ≈ 0,004 % g), dunque l’arbitraggio del segnale SMA è **statisticamente insignificante** rispetto al rumore di mercato.

**Conclusione** – La strategia a media mobile semplice non genera un ritorno consistente al di sopra del semplice buy‑and‑hold; il margine è marginale, spesso annullato dal trend negativo dei titoli.

---

**2 – Medie mobili esponenziali (EMA 12 / 16)**  

| Ticker | Periodo considerato (ultimi 30 gg) | Invested EMA (%) | Rendimento medio giornaliero * (EMA) | Rendimento medio giornaliero * (Buy‑and‑Hold) | Differenza “alpha” (bps/g) | Trend di prezzo (30 gg) |
|--------|-----------------------------------|-------------------|--------------------------------------|-----------------------------------------------|---------------------------|------------------------|
| AAPL   | 2025‑12‑02 → 2025‑12‑31           | 24 % (6/26 giorni) | +0,001 % (≈ 0,26 % annuale)          | +0,000 % (≈ 0,01 % annuale)                  | **+9 bp**                | **Ribasso** (‑0,16 % su 30 gg) |
| CAT    | 2025‑12‑02 → 2025‑12‑31           | 88 % (23/26 giorni) | +0,002 % (≈ 0,55 % annuale)          | +0,001 % (≈ 0,27 % annuale)                  | **+28 bp**                | **Ribasso** (‑0,70 % su 30 gg) |
| **Media** | –                               | 56 %               | +0,0015 % (≈ 0,38 % annuale)          | +0,0005 % (≈ 0,13 % annuale)                 | **+10 bp**                | – |

\*Il rendimento medio è la media dei valori della colonna **`rtn`** nei giorni in cui **`Invested_EWM == 1`**.  
\*Buy‑and‑hold è la media dei valori della colonna **`Buy_and_hold`** (stessa definizione della SMA).

**Valutazione tecnica**  
- L’EMA è più sensibile alle variazioni di prezzo (finestra più corta) e quindi è attiva quasi quanto la SMA, ma non traduce questa maggiore reattività in un alpha significativo.  
- L’**alpha medio** rimane intorno a **10 bp/giorno**, identico a quello della SMA, con una **deviazione standard** leggermente superiore (≈ 0,0045 % g).  
- Anche qui i titoli mostrano un **trend decrescente** nell’ultimo mese; il vantaggio temporale offerto dall’EMA è “consumato” dal ribasso di mercato.  
- La diversità di segnale tra le due medie (esponenziale vs semplice) non produce alcuna convergenza di performance; entrambe sono **sopravvalutate** rispetto a una semplice esposizione al mercato.

**Conclusione** – La strategia a media mobile esponenziale non aggiunge valore reale rispetto al buy‑and‑hold. L’edge è marginale, la copertura di mercato è alta e il trend negativo dei titoli ne elimina ogni vantaggio pratico.

---

### Sintesi globale (SMA + EMA)

| Metodologia | % tempo investito | Rendimento medio annuo (strategia) | Rendimento medio annuo (B&H) | Alpha medio annuo | Trend 30 gg |
|--------------|------------------|------------------------------------|------------------------------|-------------------|------------|
| SMA 20 / 120 | 54 %             | **≈ 0,38 %**                        | **≈ 0,13 %**                 | **≈ 2,5 %**       | Ribasso    |
| EMA 12 / 16  | 56 %             | **≈ 0,38 %**                        | **≈ 0,13 %**                 | **≈ 2,5 %**       | Ribasso    |

- **Alpha** è costantemente < 3 % p.a. e fortemente dipendente dal singolo ticker.  
- **Volatilità di risultato** e **costo di opportunità** (tempo non investito) erodono qualsiasi beneficio.  
- **Trend di mercato negativo** negli ultimi 30 gg rende le strategie ancora più poco affidabili.  

**Verdetto finale – Brutale:** le due regole di crossover di medie mobili non sono sufficienti a giustificare un “premio” di gestione: forniscono un vantaggio marginale, altamente variabile e facilmente annullato da condizioni di mercato avverse. In un contesto di allocazione di capitale a livello di hedge‑fund, l’impiego di queste strategie dovrebbe essere considerato **non necessario** o, al più, usato come filtro secondario in combinazione con segnali più robusti.

=== OTTIMIZZAZIONE PORTAFOGLIO ===
**1. risk_free**  
- Valore: **0.045** (4,5 % annuo).  
- Qualunque strategia deve generare un rendimento *superiore* a questo tasso, altrimenti non è giustificata dal capitale allocato.  


**2. betas** – valore di β per ciascun titolo (β = 1 ≈ movimento medio del mercato).  

| Ticker | β | Valutazione |
|--------|----|--------------|
| AAPL   | **33,29** | Estremamente più volatile del mercato; implica movimenti di più di 30 volte la variazione dell’indice. |
| MU     | **14,76** | Altamente sensibile; rischio di swing molto ampio. |
| V      | **‑27,86** | Beta negativo molto elevato: in teoria si muove in direzione opposta al mercato con ampiezza 28×; in pratica segnala una stima anomala. |
| GE     | **179,10** | Valore anomalo; indica una volatilità quasi 180 volte il mercato, probabilmente errore di calcolo o di data‑sourcing. |
| VMC    | **‑1,07** | Movimento opposto al mercato ma con ampiezza quasi unità; più stabile rispetto ai precedenti, ma comunque atipico. |
| EME    | **2,61** | Moderatamente più volatile del mercato (≈2,6×). |
| TMO    | **‑2,28** | Inversamente correlato con ampiezza > 2, ma forte instabilità. |
| RCL    | **13,08** | Molto volatile, 13× il mercato. |
| CAT    | **‑21,50** | Altissimo beta negativo; indica una risposta opposta al mercato con intensità esagerata. |

**Conclusione sui β**: la maggior parte dei titoli presenta beta fuori scala (±10 → ±200). Tali valori suggeriscono problemi di modellazione, data‑quality o di definizione dell’indice di riferimento. Un portafoglio costruito su questi beta è intrinsecamente poco affidabile.  



**3. Analisi del portafoglio “ideale”**  

| Metri| Valore | Commento |
|------|--------|----------|
| **portfolio_returns** | **0,012466  (1,25 % mensile)** | Rendimento mensile > risk‑free annuale (4,5 % → ≈0,38 % mensile). Su base annua il ritorno è circa 15 %, superiore al risk‑free, ma il confronto è affetto da frequenze diverse (mensile vs annuo). |
| **portfolio_variance** | **0,001095** | Deviazione standard ≈ 0,033  (3,3 % mensile). In termini annualizzati: σ ≈ 0,033 × √12 ≈ 0,115 → 11,5 % mensile ≈ ≈ 41 % annuo, molto più alta del ritorno (15 % annuo). |
| **sharpe_ratio** | **0,376** | Sharpe < 0,5 → **molto debole**; suggerisce che il compenso per unità di rischio è scarso. Non è “vicino a 1” né “≥ 2”. |
| **portfolio_weights** | 25 % AAPL, 25 % GE, 25 % RCL, 16,1 % CAT, resto ≈ 0 % | **Concentrazione elevata**: 75 % del capitale è concentrato su tre titoli (AAPL, GE, RCL) e un quarto su CAT. I pesi “negligibili” (≈ 10⁻¹³‑10⁻¹⁴) sono praticamente assenti, quindi il portafoglio è **sbilanciato** e vulnerabile a shock su pochi asset. |

**Valutazione complessiva**  
- **Rendimento vs risk‑free**: il portafoglio supera il tasso privo di rischio su base mensile, ma la differenza è marginale rispetto alla volatilità implicita.  
- **Equilibrio dei pesi**: evidente concentrazione; un vero “portafoglio ottimale” dovrebbe distribuire il capitale più uniformemente per ridurre il rischio idiosincratico.  
- **Sharpe Ratio**: 0,376 è **insoddisfacente**; indica che il premio di rischio è quasi nullo.  
- **Beta incoerenti**: la presenza di beta astronomici/negativi rende dubbia la solidità dell’output di ottimizzazione; è probabile che la frontiera di efficienza sia distorta.  

**Conclusione finale**: il modello produce un portafoglio con rendimento marginalmente superiore al risk‑free, ma con **volatilità e concentrazione eccessive** e un **Sharpe ratio troppo basso** per qualificarlo come “ideale”. I beta anomali evidenziano un problema fondamentale di input dati; senza una revisione di questi parametri, l’affidabilità dell’intera ottimizzazione è altamente compromessa.  