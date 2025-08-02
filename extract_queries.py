#!/usr/bin/env python3
"""
Script per estrarre la colonna A da domande chatbot.xlsx e salvarla in queries.txt
"""

import pandas as pd
import sys
import os

def extract_queries_from_excel(excel_file, output_file):
    """
    Estrae la colonna A da un file Excel e la salva in un file di testo.
    
    Args:
        excel_file (str): Percorso del file Excel
        output_file (str): Percorso del file di output
    """
    try:
        # Carica il file Excel
        print(f"Caricamento file Excel: {excel_file}")
        df = pd.read_excel(excel_file)
        
        # Estrai la prima colonna (colonna A)
        first_column = df.iloc[:, 0]
        
        # Filtra valori non nulli e non vuoti
        queries = [str(q).strip() for q in first_column if pd.notna(q) and str(q).strip()]
        
        print(f"Trovate {len(queries)} domande nella colonna A")
        
        # Salva nel file di testo
        with open(output_file, 'w', encoding='utf-8') as f:
            for query in queries:
                f.write(query + '\n')
        
        print(f"Domande salvate in: {output_file}")
        
        # Mostra alcune domande di esempio
        print("\nPrime 5 domande estratte:")
        for i, query in enumerate(queries[:5], 1):
            print(f"{i}. {query}")
        
        if len(queries) > 5:
            print(f"... e altre {len(queries) - 5} domande")
        
        return True
        
    except FileNotFoundError:
        print(f"Errore: File {excel_file} non trovato.")
        return False
    except Exception as e:
        print(f"Errore durante l'estrazione: {e}")
        return False

def main():
    """Funzione principale."""
    excel_file = "domande chatbot.xlsx"
    output_file = "queries.txt"
    
    # Controlla se il file Excel esiste
    if not os.path.exists(excel_file):
        print(f"Errore: File '{excel_file}' non trovato nella directory corrente.")
        print("Assicurati che il file sia presente e riprova.")
        sys.exit(1)
    
    # Estrai le domande
    success = extract_queries_from_excel(excel_file, output_file)
    
    if success:
        print(f"\n✅ Estrazione completata con successo!")
        print(f"File creato: {output_file}")
    else:
        print(f"\n❌ Errore durante l'estrazione.")
        sys.exit(1)

if __name__ == "__main__":
    main()