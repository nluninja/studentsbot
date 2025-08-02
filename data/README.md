# Data Directory 📊

Questa cartella contiene i file di dati utilizzati per testare e alimentare il StudentsBot.

## 📄 File Presenti

### `domande chatbot.xlsx`
- **Descrizione**: File Excel con domande di test per il chatbot
- **Formato**: Excel (.xlsx)
- **Contenuto**: 56 domande nella colonna A
- **Utilizzo**: Input per batch processing e testing
- **Esempio**: 
  ```bash
  python batch_query.py "data/domande chatbot.xlsx" risultati.json
  ```

### `queries.txt`
- **Descrizione**: Domande estratte dal file Excel, una per riga
- **Formato**: Testo semplice (.txt)
- **Contenuto**: 56 domande in italiano
- **Codifica**: UTF-8
- **Generato da**: `python extract_queries.py`
- **Esempio**:
  ```bash
  python batch_query.py data/queries.txt risultati.csv
  ```

## 🔧 Utilizzo

### Estrazione Domande da Excel
```bash
# Estrae la colonna A da Excel e crea queries.txt
python extract_queries.py
```

### Elaborazione Batch
```bash
# Da Excel direttamente
python batch_query.py "data/domande chatbot.xlsx" risultati.json --verbose

# Da file di testo
python batch_query.py data/queries.txt risultati.csv
```

## 📝 Esempi di Domande

Le domande coprono vari argomenti:

- **Corsi Magistrali**: "Quali sono i corsi magistrali attivi all'Università Cattolica?"
- **Lingue**: "Quali sono i corsi magistrali in inglese?"
- **Sedi**: "Quali corsi magistrali sono disponibili a Piacenza?"
- **Esami**: "Che esami si devono sostenere nel primo anno di Data Analytics?"
- **Sbocchi**: "Quali sono gli sbocchi professionali del corso Agricultural and Food Economics?"

## 🗂️ Aggiungere Nuovi Dati

Per aggiungere nuove domande:

1. **Excel**: Modifica `domande chatbot.xlsx` (colonna A)
2. **Testo**: Aggiungi domande a `queries.txt` (una per riga)
3. **Rigenera**: Esegui `python extract_queries.py` se hai modificato l'Excel

## 📊 Formati Supportati

Il sistema supporta:
- **Excel** (.xlsx, .xls) - colonna A
- **CSV** (.csv) - prima colonna o colonna "question"
- **TXT** (.txt) - una domanda per riga
- **JSON** (.json) - array di stringhe o oggetto con campo "questions"