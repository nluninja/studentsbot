
#!/usr/bin/env python3
"""
Script per eseguire query massive al chatbot StudentsBot.
Utilizza la funzione query_chatbot estratta da bot_review.py.
"""

import sys
import os
import json
import csv
from datetime import datetime
from dotenv import load_dotenv
import pandas as pd

# Import the query function from bot_review
from bot_review import query_chatbot

def load_questions_from_file(file_path):
    """Carica le domande da un file (supporta .txt, .json, .csv, .xlsx)."""
    questions = []
    
    if file_path.endswith('.txt'):
        with open(file_path, 'r', encoding='utf-8') as f:
            questions = [line.strip() for line in f if line.strip()]
    
    elif file_path.endswith('.json'):
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            if isinstance(data, list):
                questions = data
            elif isinstance(data, dict) and 'questions' in data:
                questions = data['questions']
    
    elif file_path.endswith('.csv'):
        with open(file_path, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            questions = [row.get('question', '') for row in reader if row.get('question', '').strip()]
    
    elif file_path.endswith(('.xlsx', '.xls')):
        try:
            # Load Excel file and get column A
            df = pd.read_excel(file_path)
            # Get first column (column A)
            first_column = df.iloc[:, 0]
            questions = [str(q).strip() for q in first_column if pd.notna(q) and str(q).strip()]
        except Exception as e:
            print(f"Errore nel caricamento del file Excel: {e}")
            return []
    
    return questions

def save_results(results, output_file):
    """Salva i risultati in un file (supporta .json, .csv)."""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    
    if output_file.endswith('.json'):
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump({
                'timestamp': timestamp,
                'total_queries': len(results),
                'results': results
            }, f, ensure_ascii=False, indent=2)
    
    elif output_file.endswith('.csv'):
        with open(output_file, 'w', encoding='utf-8', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=['question', 'answer', 'timestamp'])
            writer.writeheader()
            for result in results:
                writer.writerow(result)

def batch_query(questions, verbose=False, save_to=None):
    """
    Esegue query massive al chatbot.
    
    Args:
        questions (list): Lista di domande da fare
        verbose (bool): Se stampare informazioni dettagliate
        save_to (str): Percorso file dove salvare i risultati
        
    Returns:
        list: Lista di risultati con domande e risposte
    """
    results = []
    total = len(questions)
    
    print(f"Inizio elaborazione di {total} domande...")
    
    for i, question in enumerate(questions, 1):
        if verbose:
            print(f"\n[{i}/{total}] Elaborando: {question}")
        else:
            print(f"Progresso: {i}/{total}")
        
        try:
            answer = query_chatbot(question, verbose=verbose)
            result = {
                'question': question,
                'answer': answer,
                'timestamp': datetime.now().isoformat()
            }
            results.append(result)
            
            if not verbose:
                print(f"✓ Risposta ottenuta per domanda {i}")
            
        except Exception as e:
            error_msg = f"Errore per la domanda '{question}': {e}"
            print(f"✗ {error_msg}")
            result = {
                'question': question,
                'answer': f"ERRORE: {e}",
                'timestamp': datetime.now().isoformat()
            }
            results.append(result)
    
    print(f"\nElaborazione completata. {len(results)} risultati ottenuti.")
    
    # Salva risultati se richiesto
    if save_to:
        save_results(results, save_to)
        print(f"Risultati salvati in: {save_to}")
    
    return results

def main():
    """Funzione principale per uso da linea di comando."""
    load_dotenv()
    
    if len(sys.argv) < 2:
        print("Uso: python batch_query.py <file_domande> [output_file] [--verbose]")
        print("Formati supportati: .txt, .json, .csv, .xlsx, .xls")
        print("Esempi:")
        print("  python batch_query.py domande.txt")
        print("  python batch_query.py domande.xlsx risultati.csv")
        print("  python batch_query.py 'domande chatbot.xlsx' risultati.json --verbose")
        sys.exit(1)
    
    questions_file = sys.argv[1]
    output_file = sys.argv[2] if len(sys.argv) > 2 and not sys.argv[2].startswith('--') else None
    verbose = '--verbose' in sys.argv
    
    if not os.path.exists(questions_file):
        print(f"Errore: File {questions_file} non trovato.")
        sys.exit(1)
    
    # Carica domande
    try:
        questions = load_questions_from_file(questions_file)
        if not questions:
            print("Errore: Nessuna domanda trovata nel file.")
            sys.exit(1)
    except Exception as e:
        print(f"Errore nel caricamento delle domande: {e}")
        sys.exit(1)
    
    # Esegui batch query
    results = batch_query(questions, verbose=verbose, save_to=output_file)
    
    # Mostra statistiche finali
    successful = len([r for r in results if not r['answer'].startswith('ERRORE:')])
    print(f"\nStatistiche finali:")
    print(f"- Domande elaborate: {len(results)}")
    print(f"- Risposte riuscite: {successful}")
    print(f"- Errori: {len(results) - successful}")

if __name__ == "__main__":
    main()