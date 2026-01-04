# client.py
# File che racchiuderà le funzioni di chiamate agli LLM

import ollama
from .json_creator import JsonCreator

class LlmClient:

    # Funzione per la valutazione dei dati iniziali
    @staticmethod
    def evaluate_data(all_data_tail, rend_com, cum_daily_return, llm, tickers, years):

        dati = JsonCreator.data_json(all_data_tail, rend_com, cum_daily_return, tickers, years)
        # Prompt da usare
        prompt_data = f"""
        Agisci come un Chief Investment Officer (CIO) di un hedge fund quantitativo. 
        Il tuo compito è analizzare i seguenti dati relativi alle performance storiche di alcuni titoli:
        
        {dati}
        
        --- RICHIESTA ANALISI PER OGNI DATO ---
        1. Per 'latest_data' fai un breve riassunto dei dati per ogni titolo, spiegando cosa è successo
        2. Per 'compound_returns' spiega brevemente ogni titolo come si è comportato e indica anche, per ogni titolo, quanto è buono quel valore.
           Considera buoni i valori intorno a 0,07 per ogni anno trascorso, ottimi i valori sopra 0,15 e bassi i valori sotto 0,04 per ogni anno trascorso.
           Il valore in input è in percentuale, dove 1,00 è 100%.
        3. Per 'cumulative_return_last' indica per ogni titolo il valore ottenuto, indicando il lettore di effettuare un confronto con 'compound_returns'
           dare però opinioni.
        
        Rispondi in modo asciutto, tecnico e privo di bias ottimisti. Sii brutale nella valutazione dei dati.
        Non interpretare valori di prezzo come rendimento, non formulare raccomandazioni di investimento e se una metrica non è definita formalmente, non usarla.
        """

        try:
            print("Effettuando l'analisi della performance storica...")
            response = ollama.chat(model=llm, messages=[
                {'role': 'user', 'content': prompt_data}
            ])

            print("\n--- ANALISI DATI INIZIALI COMPLETATA ---")
            return response['message']['content']

        except Exception as e:
            print(f"\nErrore durante la chiamata a Ollama: {e}")


    # Funzione per la valutazione delle statistiche
    @staticmethod
    def evaluate_analytics(statistics, corr_matrix, cov_matrix, llm, tickers):

        dati = JsonCreator.analytics_json(statistics, corr_matrix, cov_matrix, tickers)
        # Prompt da usare
        prompt_analytics = f"""
        Agisci come un Chief Investment Officer (CIO) di un hedge fund quantitativo. 
        Il tuo compito è analizzare i seguenti dati relativi alle statistiche ed all'esposizione al rischio di alcuni titoli:
        
        {dati}
        
        --- RICHIESTE DI ANALISI CRITICA ---
        1. Per 'statistics' esponi ogni statistica per ogni titolo;
        2. Per 'correlation_matrix' esponi la tabella e valuta i titoli con correlazione maggiore e minore. Considera che
        valori più vicini ad 1 indicano più correlazione e minor diversificazione, mentre valori prossimi allo 0 indicano un'ottima
        diversificazione dei due titoli;
        3. Per 'covariance_matrix' esponi la tabella e indica quali titoli hanno ottenuto i valori più alti e più bassi, considerando sempre
        che valori più bassi indicano un minor rischio all'interno del portfolio e viceversa.

        Le statistiche di media, deviazione standard e varianza sono calcolate come rolling statistics su una finestra di osservazioni giornaliere.
        Non si tratta di statistiche full-sample.
        
        Rispondi in modo asciutto, tecnico e privo di bias ottimisti. Sii brutale nella valutazione delle statistiche.
        Non interpretare valori di prezzo come rendimento, non formulare raccomandazioni di investimento e se una metrica non è definita formalmente, non usarla.
        """
        try:
            print("Effettuando l'analisi dei rischi...")
            response = ollama.chat(model=llm, messages=[
                {'role': 'user', 'content': prompt_analytics}
            ])

            print("\n--- ANALISI RISCHI COMPLETATA ---")
            return response['message']['content']

        except Exception as e:
            print(f"\nErrore durante la chiamata a Ollama: {e}")


    # Funzione per l'analisi delle strategie
    @staticmethod
    def evaluate_signals(sma, ewm, llm, sma_low, sma_high, ewm_low, ewm_high):

        dati = JsonCreator.signal_json(sma, ewm, sma_low, sma_high, ewm_low, ewm_high)
        # Prompt da usare
        prompt_signals = f"""
        Agisci come un Chief Investment Officer (CIO) di un hedge fund quantitativo. 
        Il tuo compito è analizzare i seguenti dati relativi alle strategie di investimento per ogni ticker:
        
        {dati}
        
        --- RICHIESTE DI ANALISI CRITICA ---
        1. Per 'medie_mobili_semplici' indica i rendimenti ricavati rapportati alle finestre usate e di come abbiano performato 
        rispetto alla strategia buy and hold, indicando anche se nell'ultimo periodo i titoli stanno crescendo (valori in rialzo) 
        o diminuendo (valori al ribasso);
        2. Per 'medie_mobili_esponenziali' indica i rendimenti ricavati rapportati alle finestre usate e di come abbiano performato 
        rispetto alla strategia buy and hold, indicando anche se nell'ultimo periodo i titoli stanno crescendo (valori in rialzo) 
        o diminuendo (valori al ribasso).
        
        Rispondi in modo asciutto, tecnico e privo di bias ottimisti. Sii brutale nella valutazione delle strategie.
        Non interpretare valori di prezzo come rendimento, non formulare raccomandazioni di investimento e se una metrica non è definita formalmente, non usarla.
        """

        try:
            print("Effettuando l'analisi delle strategie...")
            response = ollama.chat(model=llm, messages=[
                {'role': 'user', 'content': prompt_signals}
            ])

            print("\n--- ANALISI STRATEGIE COMPLETATA ---")
            return response['message']['content']

        except Exception as e:
            print(f"\nErrore durante la chiamata a Ollama: {e}")

    # Funzione per l'analisi del portfolio
    @staticmethod
    def evaluate_optimizer(risk_free, betas, rit_port_best, pesi_migliori, var_port_best, llm, tickers, sharpe):

        dati = JsonCreator.optimizer_json(risk_free, betas, rit_port_best, pesi_migliori, var_port_best, tickers, sharpe)

        prompt_optimizer = f"""
        Agisci come un Chief Investment Officer (CIO) di un hedge fund quantitativo. 
        Il tuo compito è analizzare i seguenti dati relativi al calcolo di un portfolio ottimale:
        
        {dati}
        
        --- RICHIESTE DI ANALISI CRITICA ---
        1. Per 'risk_free' indicane il valore, specificando che un eventuale investimento dovrebbe avere dei ritorni superiori
        a questo valore;
        2. Per 'betas' indica il valore di ogni titolo e fanne una valutazione tenendo conto che un valore di 1 indica un movimento
        simile al mercato, più alto indica un titolo più volatile del mercato e più basso indica un valore più stabile;
        4. Per 'portfolio_returns', 'portfolio_weights', 'portfolio_variance' e 'sharp_ratio' esponi i valori ottenuti 
        specificando che si tratta dell'analisi del portfolio ideale, indicando anche se:
            - 'portfolio_returns' è maggiore a 'risk_free';
            - 'portfolio_weights' ha dei valori equilibrati e non sbilanciati (ad esempio 0,65 solo su un titolo);
            - 'sharp_ratio' è più vicino allo 0 (si guadagna meno del risk_free), più vicino ad 1 (valore buono) o uguale/superiore a 2 (valore eccellente).
        
        Rispondi in modo asciutto, tecnico e privo di bias ottimisti. Sii brutale nella valutazione dei portfoli.
        Non interpretare valori di prezzo come rendimento, non formulare raccomandazioni di investimento e se una metrica non è definita formalmente, non usarla.
        """
        try:
            print("Effettuando l'analisi del portfolio...")
            response = ollama.chat(model=llm, messages=[
                {'role': 'user', 'content': prompt_optimizer}
            ])

            print("\n--- ANALISI PORTFOLIO COMPLETATA ---")
            return response['message']['content']

        except Exception as e:
            print(f"\nErrore durante la chiamata a Ollama: {e}")