# StudentsBot 🎓

Un chatbot intelligente per fornire informazioni su corsi, esami, servizi e procedure dell'Università Cattolica utilizzando tecnologie RAG (Retrieval-Augmented Generation).

## 🚀 Caratteristiche

- **Chat interattivo** per domande in linguaggio naturale
- **Elaborazione massive** di query da file Excel/CSV/TXT
- **Indicizzazione automatica** di documenti crawlati
- **Supporto multilingua** (Italiano/Inglese)
- **Modalità debug** integrate per sviluppo

## 🛠️ Tecnologie

- **LangChain** - Framework per applicazioni AI
- **Google Gemini** - Modello di linguaggio (LLM)
- **FAISS** - Vector store per ricerca semantica
- **Pandas** - Elaborazione file Excel
- **BeautifulSoup** - Web crawling

## 📦 Installazione

### Prerequisiti
- Python 3.8+
- API Key Google Gemini

### Setup Rapido
```bash
# Clona il repository
git clone https://github.com/YOUR_USERNAME/studentsbot.git
cd studentsbot

# Setup automatico
source activate_studentsbot.sh

# Configura API key (modifica .env)
GOOGLE_API_KEY=your_api_key_here

# Avvia il bot
studentsbot
```

### Setup Manuale
```bash
# Crea ambiente virtuale
python -m venv venv
source venv/bin/activate

# Installa dipendenze
pip install -r requirements.txt

# Configura environment
cp .env.example .env
# Modifica .env con la tua GOOGLE_API_KEY
```

## 🚀 Utilizzo

### Modalità Interattiva
```bash
# Prima configurazione
python bot_review.py --index_only       # Crea vectorstore
python bot_review.py --interactive      # Avvia chat

# Configurazione guidata
python bot_review.py                    # Modalità default

# Aiuto completo
python bot_review.py --help
```

### Elaborazione Massive
```bash
# Da file Excel (colonna A)
python batch_query.py "domande.xlsx" risultati.json --verbose

# Da file di testo
python batch_query.py queries.txt risultati.csv

# Estrai domande da Excel
python extract_queries.py  # crea queries.txt
```

### Web Crawling
```bash
# Raccolta dati dal sito web
python crawler.py
```

## 📁 Struttura Progetto

```
studentsbot/
├── 🤖 bot_review.py           # Bot principale con interfaccia
├── 📊 batch_query.py          # Elaborazione massive query
├── 🕷️ crawler.py              # Web crawler per raccolta dati
├── 📋 extract_queries.py      # Estrazione domande da Excel
├── 📝 queries.txt            # Domande estratte (56 domande)
├── 📄 domande chatbot.xlsx   # File Excel con domande
├── 📁 output_crawler/        # Documenti crawlati (150+ file)
├── 🗄️ index/                 # Vectorstore FAISS (generato)
├── 🐍 venv/                  # Ambiente virtuale Python
├── ⚙️ activate_studentsbot.sh # Script setup automatico
├── 📦 requirements.txt       # Dipendenze Python
├── 📖 README.md              # Documentazione
├── 🚫 .gitignore            # File da ignorare
├── ⚙️ .env.example          # Template variabili ambiente
└── 📄 LICENSE               # Licenza MIT
```

## 🎯 Comandi Disponibili

### Bot Principale
| Comando | Descrizione |
|---------|-------------|
| `python bot_review.py --help` | Mostra aiuto completo |
| `python bot_review.py --interactive` | Chat diretto (veloce) |
| `python bot_review.py --index_only` | Solo indicizzazione |
| `python bot_review.py` | Configurazione guidata |

### Elaborazione Batch
| Formato | Esempio |
|---------|---------|
| Excel | `python batch_query.py domande.xlsx risultati.json` |
| CSV | `python batch_query.py domande.csv risultati.json` |
| TXT | `python batch_query.py queries.txt risultati.csv` |

## 🔧 Configurazione

### File .env
```env
GOOGLE_API_KEY=your_gemini_api_key_here
```

### Parametri Bot (bot_review.py)
```python
MARKDOWN_DIR = "output_crawler"     # Directory documenti
VECTORSTORE_PATH = "index"          # Path vectorstore FAISS
MODEL_NAME_LLM = "gemini-2.5-pro"   # Modello principale
BATCH_SIZE = 100                    # Dimensione batch indicizzazione
BATCH_WAIT = 2                      # Pausa tra batch (secondi)
```

## 🐛 Debug e Sviluppo

Per il debug del codice:

1. **Modalità verbose**: Usa `--verbose` nei comandi per output dettagliato
2. **Test con sample**: Crea file di test con poche domande per debug veloce
3. **Logs**: Controlla i messaggi di errore nel terminale
4. **VSCode**: Configura il tuo ambiente di debug come preferisci

## 📊 Esempi di Domande

- "Quali sono i corsi magistrali attivi all'Università Cattolica?"
- "Quali esami ci sono nel primo anno di Data Analytics?"
- "Come posso iscrivermi a un programma Erasmus?"
- "Quali sono gli sbocchi professionali per Economia?"

## 🗂️ Dati Disponibili

- **150+ documenti** crawlati dal sito ufficiale
- **56 domande** di test estratte da Excel
- **Corsi magistrali** di tutte le sedi
- **Servizi studenti** e procedure
- **Programmi internazionali** e stage

## 🤝 Contribuire

1. Fai fork del progetto
2. Crea un branch per la feature (`git checkout -b feature/AmazingFeature`)
3. Commit delle modifiche (`git commit -m 'Add some AmazingFeature'`)
4. Push del branch (`git push origin feature/AmazingFeature`)
5. Apri una Pull Request

## 📝 Licenza

Questo progetto è rilasciato sotto licenza MIT. Vedi il file `LICENSE` per dettagli.

## 🆘 Supporto

Se hai problemi o domande:

1. Controlla la [documentazione](#-utilizzo)
2. Cerca nelle [Issues](https://github.com/YOUR_USERNAME/studentsbot/issues)
3. Apri una nuova issue se necessario

## 🙏 Ringraziamenti

- [LangChain](https://langchain.com/) per il framework AI
- [Google](https://ai.google.dev/) per l'API Gemini
- [Università Cattolica](https://www.unicatt.it/) per i dati

---

⭐ **Star questo progetto se ti è stato utile!**