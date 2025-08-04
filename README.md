# StudentsBot 🎓

An intelligent chatbot to provide information about courses, exams, services and procedures of Università Cattolica using RAG (Retrieval-Augmented Generation) technologies.

## 🎓 Academic Context

This work was developed by **Eleonora Farolfi** during his thesis work, under the supervision of **Prof. Andrea Belli** at **Università Cattolica del Sacro Cuore**.

## 🚀 Features

- **Interactive chat** for natural language questions
- **Batch processing** of queries from Excel/CSV/TXT files
- **Automatic indexing** of crawled documents
- **Multi-language support** (Italian/English)
- **Integrated debug modes** for development

## 🛠️ Technologies

- **LangChain** - Framework for AI applications
- **Google Gemini** - Language model (LLM)
- **FAISS** - Vector store for semantic search
- **Pandas** - Excel file processing
- **BeautifulSoup** - Web crawling

## 📦 Installation

### Prerequisites
- Python 3.8+
- Google Gemini API Key

### Quick Setup
```bash
# Clone the repository
git clone https://github.com/nluninja/studentsbot.git
cd studentsbot

# Automatic setup
source activate_studentsbot.sh

# Configure API key (edit .env)
GOOGLE_API_KEY=your_api_key_here

# Start the bot
studentsbot
```

### Manual Setup
```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Configure environment
cp .env.example .env
# Edit .env with your GOOGLE_API_KEY
```

## 🚀 Usage

### Interactive Mode
```bash
# Initial configuration
python bot_review.py --index_only       # Create vectorstore
python bot_review.py --interactive      # Start chat

# Guided configuration
python bot_review.py                    # Default mode

# Full help
python bot_review.py --help
```

### Batch Processing
```bash
# From Excel file (column A)
python batch_query.py "data/domande chatbot.xlsx" risultati.json --verbose

# From text file
python batch_query.py data/queries.txt risultati.csv

# Extract questions from Excel
python extract_queries.py  # creates data/queries.txt
```

### Web Crawling
```bash
# Data collection from website
python crawler.py
```

### 📊 Response Evaluation

The project includes several tools to evaluate the quality of chatbot responses:

#### 1. Automatic Evaluation (rageval.py)
```bash
# Complete evaluation with multiple metrics
python rageval.py risultati.json

# Save detailed results
python rageval.py risultati.json valutazione_dettagliata.json
```

**Calculated metrics:**
- **Text similarity** (difflib SequenceMatcher)
- **ROUGE-1, ROUGE-2, ROUGE-L** (n-gram overlap and LCS)
- **BLEU score** (precision with brevity penalty)
- **Keyword overlap** (precision, recall, F1)

#### 2. LLM-as-Judge Evaluation (llm_as_judge.py)
```bash
# Use LLM model to judge semantic equivalence
python llm_as_judge.py risultati.json

# Save detailed judgments
python llm_as_judge.py risultati.json -o giudizi_llm.json
```

**LLM Judge features:**
- Intelligent semantic evaluation
- Confidence score for each judgment
- Detailed reasoning for decisions
- Robust error handling

## 📁 Project Structure

```
studentsbot/
├── 🤖 bot_review.py           # Main bot with interface
├── 📊 batch_query.py          # Batch query processing
├── 🕷️ crawler.py              # Web crawler for data collection
├── 📋 extract_queries.py      # Extract questions from Excel
├── 📊 rageval.py              # Complete evaluation (ROUGE, BLEU, etc)
├── 🧠 llm_as_judge.py         # Semantic evaluation with LLM
├── 📁 data/                  # Input and test data
│   ├── 📄 domande chatbot.xlsx  # Excel file with questions
│   └── 📝 queries.txt          # Extracted questions (56 questions)
├── 📁 output_crawler/        # Crawled documents (150+ files)
├── 🗄️ index/                 # FAISS vectorstore (generated)
├── 🐍 venv/                  # Python virtual environment
├── ⚙️ activate_studentsbot.sh # Automatic setup script
├── 📦 requirements.txt       # Python dependencies
├── 📖 README.md              # Documentation
├── 🚫 .gitignore            # Files to ignore
├── ⚙️ .env.example          # Environment variables template
└── 📄 LICENSE               # MIT License
```

## 🎯 Available Commands

### Main Bot
| Command | Description |
|---------|-------------|
| `python bot_review.py --help` | Show complete help |
| `python bot_review.py --interactive` | Direct chat (fast) |
| `python bot_review.py --index_only` | Indexing only |
| `python bot_review.py` | Guided configuration |

### Batch Processing
| Format | Example |
|---------|---------|
| Excel | `python batch_query.py data/domande.xlsx risultati.json` |
| CSV | `python batch_query.py data/domande.csv risultati.json` |
| TXT | `python batch_query.py data/queries.txt risultati.csv` |

## 🔧 Configuration

### .env File
```env
GOOGLE_API_KEY=your_gemini_api_key_here
```

### Bot Parameters (bot_review.py)
```python
MARKDOWN_DIR = "output_crawler"     # Documents directory
VECTORSTORE_PATH = "index"          # FAISS vectorstore path
MODEL_NAME_LLM = "gemini-2.5-pro"   # Main model
BATCH_SIZE = 100                    # Indexing batch size
BATCH_WAIT = 2                      # Pause between batches (seconds)
```

## 🐛 Debug and Development

For code debugging:

1. **Verbose mode**: Use `--verbose` in commands for detailed output
2. **Sample testing**: Create test files with few questions for quick debug
3. **Logs**: Check error messages in terminal
4. **VSCode**: Configure your debug environment as preferred

## 📊 Sample Questions

- "What are the active master's degree courses at Università Cattolica?"
- "What exams are there in the first year of Data Analytics?"
- "How can I enroll in an Erasmus program?"
- "What are the career opportunities for Economics?"

## 🗂️ Available Data

- **150+ documents** crawled from official website
- **56 test questions** extracted from Excel
- **Master's degree courses** from all campuses
- **Student services** and procedures
- **International programs** and internships

## 🤝 Contributing

1. Fork the project
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is released under the MIT License. See the `LICENSE` file for details.

## 🆘 Support

If you have problems or questions:

1. Check the [documentation](#-usage)
2. Search in [Issues](https://github.com/YOUR_USERNAME/studentsbot/issues)
3. Open a new issue if necessary

## 🙏 Acknowledgments

- [LangChain](https://langchain.com/) for the AI framework
- [Google](https://ai.google.dev/) for the Gemini API
- [Università Cattolica](https://www.unicatt.it/) for the data


---

⭐ **Star this project if it was useful to you!**