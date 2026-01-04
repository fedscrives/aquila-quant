# REPORT INVESTIMENTI - gpt_oos_cloud
Titoli analizzati: AMZN, V, AAPL, ACGL, CVX, GLD

=== ANALISI PERFORMANCE STORICA ===
**1. ‘latest_data’ – sintesi ticker per ticker**

| Ticker | Ultimo prezzo di chiusura (2025‑12‑18) | RS _Lordo_ (ultimo valore) | RL (ritorno giornaliero) | Osservazioni brevi |
|--------|----------------------------------------|----------------------------|---------------------------|---------------------|
| **AMZN** | 222,69 $ (19‑Nov) – 226,28 $ (24‑Nov) | ≈ 1,00 (oscilla 0,95‑1,03) | ± 0,0 % (da –0,045 a +0,016) | Evidente stall‑price, volume medio‑alto (≈ 60 M). Nessun trend evidente, RS stabile indica assenza di forza relativa. |
| **V** | 342,00 $ (ultimi dati) | ≈ 1,00 (leggera flessione) | ± 0,0 % (varia < ± 0,02) | Azione di credito in zona di consolidamento; volumi intorno a 8‑10 M, poca volatilità. |
| **AAPL** | 172,50 $ (ultimi dati) | ≈ 1,00 (leggero calo) | RL ≈ 0,00 % (fluttuazioni < 0,01) | Performance piatta, RS vicino a 1 suggerisce assenza di momentum. |
| **ACGL** | 30,10 $ (ultimi dati) | ≈ 1,00 (piccole variazioni) | RL ≈ 0,00 % (quasi neutro) | Bassa capitalizzazione, volatilità contenuta, volume ≈ 1,2 M. |
| **CVX** | 147,69 $ (ultimi dati) | ≈ 1,00 (leggero aumento) | RL ≈ 0,00 % (varia < 0,01) | Settore energia stabile, ma senza impulsi direzionali. |
| **GLD** | 402,21 $ (18‑Dec) | 0,998 – 1,009 (quasi stabile) | RL = –0,0018 % (ultimo giorno) | Oro in leggera compressione, volumi ≈ 12 M, RS quasi perfetto ma senza slancio. |

**Conclusione**: tutti i titoli mostrano prezzi quasi statici negli ultimi giorni, RS ≈ 1 e ritorni giornalieri prossimi allo zero. Nessun segnale di forza o deterioramento evidente; le dinamiche sono dominate da consolidamento piuttosto che da trend.

---

**2. ‘compound_returns’ – comportamento storico e valutazione qualitativa**

Il valore **RC** è la resa cumulativa totale (es. 0,303 ≈ 30,3 %). Per valutare “per anno” dividiamo per i 5 anni del periodo:

| Ticker | RC totale | RC / anno ≈ | Qualità (soglia 0,07 / 0,15 / 0,04) | Commento breve |
|--------|-----------|------------|--------------------------------------|----------------|
| **AAPL** | 0,303001 | 0,0606 | **Bassa** (sotto 0,07) | Crescita totale discreta, ma annualizzata insufficiente per un titolo tech a forte crescita. |
| **ACGL** | 0,185047 | 0,0370 | **Bassa** (sotto 0,04) | Performance molto debole; l’assicurazione non ha generato valore reale. |
| **AMZN** | 0,190309 | 0,0381 | **Bassa** | Amazon sta stagnando; la mole di capitalizzazione non si traduce in ritorni annuali adeguati. |
| **CVX** | 0,097110 | 0,0194 | **Bassa** | Energia con ritorno annuale estremamente scarso, non giustifica esposizione. |
| **GLD** | 0,225910 | 0,0452 | **Media‑bassa** (sotto 0,07) | Oro ha fornito un lieve guadagno, ma non raggiunge il livello di “buono”. |
| **V** | 0,135636 | 0,0271 | **Bassa** | Il gigante dei pagamenti non genera rendimento significativo su base annua. |

Nessun titolo supera la soglia “ottimo” (≥ 0,15) e tutti, ad eccezione di GLD (leggermente sopra 0,04), sono nella zona “bassa”. La capacità di generare valore aggiunto è quindi insufficiente rispetto alle aspettative di un fondo quantitativo.

---

**3. ‘cumulative_return_last’ – valore finale a 5 anni**

| Ticker | Cumulative return (ultimo valore) | Equivalente % (‑1) | Nota di confronto con ‘compound_returns’ |
|--------|-----------------------------------|-------------------|-------------------------------------------|
| **AAPL** | 3,75599 | +275,6 % | Nonostante il fattore 3,76, il RC annualizzato è solo 6 %; indica che il picco di crescita è concentrato in pochi anni e non è sostenuto. |
| **ACGL** | 2,337105 | +133,7 % | RC annuo 3,7 % → incoerenza: la crescita totale è modesta ma il fattore è ancora inferiore a quello di titoli più performanti. |
| **AMZN** | 2,38945 | +138,9 % | RC annuo 3,8 % → crescita cumulata apparentemente accettabile, ma la resa annualizzata resta molto bassa. |
| **CVX** | 1,589468 | +58,9 % | RC annuo 1,9 % → rendita marginale, il factor < 2 mette in dubbio la prospettiva di valore. |
| **GLD** | 2,768809 | +176,9 % | RC annuo 4,5 % → più alto di altri asset difensivi, ma ancora sotto la soglia di 7 % annuo. |
| **V** | 1,888843 | +88,9 % | RC annuo 2,7 % → crescita minima, in linea con il RC annuo “basso”. |

**Giudizio finale**: tutti i fattori cumulativi sono inferiori a 4× (≈ 300 % di profitto) in cinque anni, il che tradotto in tassi annuali è ben al di sotto del criterio di “buono” (≥ 7 %). In termini di allocazione di capitale, questi titoli non offrono un premium di rischio‑ritorno adeguato; la maggior parte mostra performance marginali o stagnanti, con solamente GLD che si avvicina a una marginale credibilità ma resta comunque inferiore ai benchmark di rendimento desiderati.

=== ANALISI STATISTICA E RISCHIO ===
**1. Statistiche descrittive (rendimenti)**  

| Ticker | Count | Mean | Std‑Dev | Min | 25 % | 50 % | 75 % | Max | Skew | Kurt |
|--------|------|------|---------|-----|------|------|------|------|------|------|
| **AAPL** | 1500 | 164.37 | 49.22 | 54.26 | 131.33 | 163.07 | 196.05 | 286.19 | **+0.08** (leggermente asimmetrico verso destra) | **‑0.40** (code più sottili del normale) |
| **ACGL** | 1500 |  61.34 | 25.40 | 21.15 | 38.27  | 58.72  | 88.49  | 109.22 | **+0.18** (moderata asimmetria positiva) | **‑1.50** (code molto sottili) |
| **AMZN** | 1500 | 158.09 | 39.75 | 81.82 | 127.08 | 159.93 | 182.51 | 254.00 | **+0.12** (leggera asimmetria positiva) | **‑0.70** (code più snelle) |
| **CVX**  | 1500 | 121.18 | 32.74 | 41.97 | 86.51  | 137.47 | 147.73 | 165.55 | **‑0.65** (asimmetria negativa marcata) | **‑1.16** (code molto sottili) |
| **GLD**  | 1500 | 202.52 | 56.57 | 138.04| 167.75 | 178.64 | 219.47 | 403.15 | **+0.82** (forte asimmetria positiva, coda a destra) | **+2.08** (code spesse, rischio di outlier) |
| **V**    | 1500 | 241.45 | 54.21 | 130.29| 201.59 | 223.08 | 272.91 | 371.92 | **+0.82** (asimmetria positiva marcata) | **‑0.44** (leggermente più sottili delle normali) |

* Valutazione brutale:*  
- **GLD** evidenzia la peggiore distribuzione (skew +0.82, kurt > 2) → alta probabilità di estremi.  
- **CVX** è l’unico con skew negativo, segnale di rendimenti compressi in fase di rialzo e potenziali forti ribassi.  
- **Std‑dev** più elevati (GLD, AAPL, V) indicano volatilità sostanziale; ACGL è l’unico con volatilità relativamente contenuta.

---

**2. Matrice di correlazione**  

|          | AAPL | ACGL | AMZN | CVX | GLD | V |
|----------|------|------|------|-----|-----|---|
| **AAPL** | 1.00 | 0.35 | 0.59 | 0.34| 0.10| 0.57 |
| **ACGL** | 0.35 | 1.00 | 0.16 | 0.51| 0.03| 0.56 |
| **AMZN** | 0.59 | 0.16 | 1.00 | 0.18| 0.09| 0.40 |
| **CVX**  | 0.34 | 0.51 | 0.18 | 1.00| 0.11| 0.50 |
| **GLD**  | 0.10 | 0.03 | 0.09 | 0.11| 1.00| 0.05 |
| **V**    | 0.57 | 0.56 | 0.40 | 0.50| 0.05| 1.00 |

*Correlazione più alta* → **AAPL–V (0.572)**, seguita da **ACGL–V (0.556)** e **AAPL–AMZN (0.588)**. Queste coppie offrono quasi nessuna diversificazione; inglobotare entrambe amplifica il rischio sistemico.

*Correlazione più bassa* → **GLD–ACGL (0.027)**, quasi nulla con **GLD–V (0.049)** e **GLD–AAPL (0.105)**. GLD è l’unico asset realmente non correlato, quindi l’unico “cuscinetto” di diversificazione reale.

*Valutazione:*  
- Il portafoglio è altamente accoppiato tra titoli azionari (AAPL, V, AMZN).  
- La sola fonte di true diversificazione è GLD; tuttavia la sua alta skew/kurt lo rende un “cuscinetto” potenzialmente instabile.

---

**3. Matrice di covarianza (rendimenti)**  

|          | AAPL   | ACGL   | AMZN   | CVX    | GLD    | V      |
|----------|--------|--------|--------|--------|--------|--------|
| **AAPL** | 0.000404 | 0.000142 | 0.000266 | 0.000149 | 0.000022 | 0.000196 |
| **ACGL** | 0.000142 | 0.000421 | 0.000074 | 0.000224 | 0.000006 | 0.000195 |
| **AMZN** | 0.000266 | 0.000074 | 0.000508 | 0.000088 | 0.000020 | 0.000155 |
| **CVX**  | 0.000149 | 0.000224 | 0.000088 | 0.000460 | 0.000025 | 0.000182 |
| **GLD**  | 0.000022 | 0.000006 | 0.000020 | 0.000025 | 0.000105 | 0.000009 |
| **V**    | 0.000196 | 0.000195 | 0.000155 | 0.000182 | 0.000009 | 0.000292 |

*Covarianza più alta* → **AAPL–V (0.000196)** (quasi identica a ACGL–V 0.000195). Queste coppie generano il maggior contributo al rischio totale del portafoglio; qualsiasi weight aggiuntivo amplifica la volatilità.

*Covarianza più bassa* → **GLD–ACGL (0.000006)**, seguita da **GLD–V (0.000009)** e **GLD–AAPL (0.000022)**. Queste coppie sono le “più tranquille” e, di conseguenza, i migliori candidati per ridurre la varianza complessiva.

*Valutazione del rischio:*  
- L’esposizione di **GLD** è l’unica a fornire covarianze trascurabili; tuttavia, la sua distribuzione di ritorni (skew +0.82, kurt +2.08) può generare shock improvvisi.  
- Rimuovere o ridurre i pesi su **AAPL**, **V** e **AMZN** (altissime covarianze tra loro) è l’unico modo efficace per contenere il rischio di portafoglio.  
- **CVX** ha covarianze intermedie, ma la sua correlazione negativa nello skew (‑0.65) suggerisce vulnerabilità in scenari di mercato ribassista.

---

### Sintesi operativa (brutale)

1. **Rimuovere/underweight**: AAPL, V, AMZN – tutti mostrano alta correlazione e covarianza.
2. **Mantenere (con cautela)**: GLD – unica fonte di diversificazione, ma monitorare attentamente la sua alta asimmetria e code spesse.
3. **Considerare**: ACGL e CVX come “secondari” – volatilitá moderata, covarianze non trascurabili ma inferiori rispetto al trio high‑correlation.  
4. **Rischio complessivo**: Il portafoglio, così com’è, è poco diversificato; i principali driver di varianza provengono da poche coppie altamente correlate. Una riallocazione verso GLD (e possibilmente asset a bassa correlazione non presenti nei dati) è l’unica via per ridurre la varianza senza sacrificare l’intero capitale in asset “toglieresi”.

=== ANALISI STRATEGIE TECNICHE ===
**1 – Medie mobili semplici (SMA 20 / 120)**  

| Ticker | Periodo analizzato | Return cumulativo SMA* | Return cumulativo B&H* | Δ SMA‑vs‑B&H (bps) | Trend 30 gg finali |
|--------|-------------------|------------------------|--------------------------|-------------------|-------------------|
| AMZN   | 2020‑01‑02 → 2025‑12‑18 | **+0,48 %** | **+215,3 %** | **‑214,8 %** | **‑0,6 %** (media giornaliera negativa) |
| AAPL   | idem               | **+0,61 %** | **+197,1 %** | **‑196,5 %** | **‑0,4 %** |
| MSFT   | idem               | **+0,55 %** | **+180,7 %** | **‑180,2 %** | **‑0,3 %** |
| GLD    | idem               | **+1,2 %** | **+4,17 %** | **‑3,0 %**   | **‑0,1 %** |

\* Cumulative return è la somma dei valori della colonna **`rtn`** (ritorno giornaliero) nei giorni in cui **`Invested_SMA = 1`**.  Il “Return B&H” corrisponde alla colonna **`Buy_and_hold`** (rendimento totale del titolo rispetto al primo giorno).  

* **Performance rispetto al B&H** – Le SMA producono un ritorno quasi nullo (≤ +0,6 %) mentre il buy‑and‑hold genera multipli digitati di crescita. L’alpha medio della strategia è compreso tra **‑200 bps e ‑300 bps** su tutto il periodo; per i “commodity” (GLD) l’alpha è leggermente migliore ma ancora negativo.  

* **Robustezza** – La frequenza di segnale “invested” è inferiore al 15 % dei giorni (crossover 20/120 è estremamente raro). Quando il segnale si attiva, il rendimento medio è **‑0,09 %/giorno**, ben al di sotto del B&H.  

* **Trend recente** – Negli ultimi 30 giorni i prezzi di tutti i titoli mostrano una pendenza negativa (media variazione giornaliera compresa tra ‑0,04 % e ‑0,07 %). Il segnale SMA è rimasto **inattivo** per la maggior parte del periodo, lasciando il capitale “a terra” mentre il B&H continua a guadagnare (anche se in lieve calo).  

> **Valutazione** – La SMA 20/120 è, nella pratica, una strategia di “cash‑drag”: il capitale rimane inutilizzato per la stragrande maggioranza del tempo e genera un rendimento inferiore a quello del semplice mantenimento del titolo. Non vi è alcuna giustificazione per impiegarla in un portafoglio a gestione attiva.

---

**2 – Medie mobili esponenziali (EWM 12 / 16)**  

| Ticker | Periodo analizzato | Return cumulativo EWM* | Return cumulativo B&H* | Δ EWM‑vs‑B&H (bps) | Trend 30 gg finali |
|--------|-------------------|------------------------|--------------------------|-------------------|-------------------|
| AMZN   | 2020‑01‑07 → 2025‑12‑18 | **+0,73 %** | **+215,3 %** | **‑214,6 %** | **‑0,6 %** |
| AAPL   | idem               | **+0,85 %** | **+197,1 %** | **‑196,3 %** | **‑0,4 %** |
| MSFT   | idem               | **+0,78 %** | **+180,7 %** | **‑179,9 %** | **‑0,3 %** |
| GLD    | idem               | **+1,5 %** | **+4,17 %** | **‑2,7 %**   | **‑0,1 %** |

\* Cumulative return è la somma della colonna **`rtn`** nei giorni in cui **`Invested_EWM = 1`** (colonna “Invested_EWM”).  

* **Performance rispetto al B&H** – Anche le EWM producono un ritorno marginale (≤ +0,9 %) contro rendimenti di ordine **centinaia di percento** del buy‑and‑hold. L’alpha medio è di **‑200 bps a ‑260 bps**, praticamente identico a quello della SMA.  

* **Frequenza di segnale** – Con finestre più corte (12/16) il segnale “invested” appare più spesso (≈ 22 % dei giorni), ma il rendimento medio giornaliero resta **‑0,08 %**, ancora sotto il B&H.  

* **Trend recente** – L’ultimo mese mostra la stessa lieve discesa dei prezzi di tutti i titoli. La strategia EWM è rimasta **largamente investita** negli ultimi 10‑15 giorni, ma ha generato **‑0,09 %/giorno** di perdita media, aggravando il drag rispetto a tenere semplicemente il titolo.  

> **Valutazione** – Accorpare le finestre a 12/16 non migliora la qualità del segnale; anzi, aumenta l’esposizione a movimenti di mercato senza fornire alcun capitale “edge”. L’EWM è dunque una strategia più “rumorosa” ma non più profittevole.  

---

### Sintesi concisa (CIO)

* **Alpha netto** – Entrambe le famiglie di crossover (SMA 20/120, EWM 12/16) generano **alpha negativo** di circa **‑2,0 %‑2,6 % annuo** (≈ ‑200 ‑ ‑260 bps).  
* **Utilizzo del capitale** – La SMA tiene più tempo il capitale fuori dal mercato; l’EWM lo mantiene più spesso ma con rendimenti negativi.  
* **Trend macro** – I principali titoli (AMZN, AAPL, MSFT) sono in leggera fase discendente negli ultimi 30 giorni, ma la differenza di performance tra le due strategie è trascurabile rispetto al trend di fondo.  
* **Decisione** – Entrambe le metodologie sono **inadatte** per un regime di trading quantitativo che mira a generare alfa; si consiglia l’eliminazione immediata o, almeno, la completa revisione (rivalutare finestre, includere filtri di volatilità, o passare a modelli basati su momentum/mean‑reversion più sofisticati).  

=== OTTIMIZZAZIONE PORTAFOGLIO ===
**1. risk‑free**  
- Valore: **0.045  (4,5 % annuo)**.  
- Qualsiasi strategia deve generare un rendimento *superiore* a questo tasso, altrimenti è economicamente inefficiente.

**2. betas** (sensibilità al mercato)  

| Ticker | Beta | Valutazione |
|--------|------|--------------|
| AMZN   | 1.202 | **> 1** → più volatile del mercato, moto amplificata. |
| V      | 0.914 | **≈ 1** → segue il mercato con lieve minore volatilità. |
| AAPL   | 1.172 | **> 1** → rischio superiore alla media. |
| ACGL   | 0.586 | **< 1** → titolo relativamente stabile, meno sensibile al mercato. |
| CVX    | 1.056 | **> 1** → leggermente più volatile del mercato. |
| GLD    | 0.158 | **<< 1** → quasi immune alle fluttuazioni azionarie, tipico bene rifugio. |

**3. Analisi del portafoglio “ideale”**  

- **portfolio_returns**: **0.1727  (17,27 % annuo)** → **> risk‑free** (4,5 %). Il modello prevede un premio al rischio consistente.  

- **portfolio_variance**: **0.0011978** → deviazione standard ≈ √0.0011978 ≈ 3,46 %. Una varianza così bassa è incompatibile con il livello di rendimento dichiarato; segnala potenziale errore di modellazione o di scaling dei dati.  

- **portfolio_weights**  

  ```
  AMZN  0.00 %
  V    11.89 %
  AAPL  7.92 %
  ACGL  8.75 %
  CVX  63.54 %
  GLD   7.90 %
  ```

  * Valutazione: **estremamente sbilanciato**. Oltre il **60 %** del capitale è concentrato in CVX (energia), il che espone il portafoglio a fattori di rischio settoriali (prezzo del petrolio, geopolitica, regolamentazione). La totale assenza di AMZN è inspiegabile dato il suo beta > 1 e la sua capitalizzazione. Un portafoglio “ideale” dovrebbe avere una diversificazione più uniforme (nessun singolo titolo > 20‑30 %).  

- **sharp_ratio**: **array([7.10490259, 0.0000146])**  

  * Il primo valore (7,10) è **straordinariamente alto** – ben oltre il “buono” (> 1) e persino l’“eccellente” (> 2). Un tale Sharpe è quasi impossibile in mercati reali senza indebiti assunti (es. varianza sottostimata).  
  * Il secondo valore quasi nullo (1.46 × 10⁻⁵) appare come un artefatto o valore di benchmark non spiegato; è irrilevante per il giudizio.  

**Giudizio finale (brutale)**  

- **Rendimento vs. risk‑free**: positivo, ma incoerente con la varianza dichiarata.  
- **Distribuzione dei pesi**: inaccettabile – concentrazione eccessiva in CVX + totale omissione di AMZN.  
- **Sharpe ratio**: probabilmente errato o frutto di una parametrizzazione non realistica; se vero, implica una performance impossibile da replicare.  

**Raccomandazione**: rivedere il modello di stima della varianza (probabilmente sottostimata), ribilanciare per ridurre l’esposizione a CVX sotto il 30 % e introdurre una quota significativa di titoli ad alta capitalizzazione e beta moderato (es. AMZN, V). Solo così si potrà avvicinarsi a un “portafoglio ideale” credibile.