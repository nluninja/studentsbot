import re
from langchain.docstore.document import Document
from langchain.text_splitter import MarkdownHeaderTextSplitter
from langchain_community.document_loaders import DirectoryLoader, TextLoader


def parse_clean_exams(text):
    """Extract and clean exam information from text content."""
    results = {}
    anno = None
    tipo = "obbligatori"
    lines = text.splitlines()
    
    for idx, line in enumerate(lines):
        l = line.strip()
        if not l:
            continue
            
        # Anno riconosciuto
        m_anno = re.search(r"(primo|secondo|terzo|1°|2°|3°|first|second|third)[^\w]{0,5}(anno|year)", l, re.I)
        if m_anno:
            anno = m_anno.group(0).lower()
            
        # Tipo (elective)
        if any(x in l.lower() for x in ["a scelta", "elective", "opzionali"]):
            tipo = "a scelta"
        if any(x in l.lower() for x in ["obbligatori", "required"]):
            tipo = "obbligatori"
            
        # Riga esame pulito
        m_exam = re.match(r"-\s*([^\|].+?)(\([A-Z\-\/\d]+\))?$", l)
        if m_exam and not any(xx in m_exam.group(1).lower() for xx in ["credits", "programme", "thesis", "seminar", "cfu", "download"]):
            key = (anno or "generico", tipo)
            results.setdefault(key, []).append(m_exam.group(1).strip())
            
        # Riga tabella "| Course | nome"
        if "|" in l and not l.startswith("| ---"):
            items = [x.strip() for x in l.split("|") if x.strip()]
            if len(items) >= 2 and not any(xx in items[1].lower() for xx in ["credits", "programme", "download", "thesis", "seminar", "cfu"]):
                key = (anno or "generico", tipo)
                if items[1] and len(items[1]) > 3 and not items[1].isdigit():
                    results.setdefault(key, []).append(items[1])
                    
    # Remove duplicates
    for k in results:
        seen = set()
        results[k] = [x for x in results[k] if not (x in seen or seen.add(x))]
        
    return results


def load_and_split_documents(markdown_dir: str):
    """Load and split markdown documents into chunks."""
    loader = DirectoryLoader(
        markdown_dir,
        glob="**/*.md",
        loader_cls=TextLoader,
        loader_kwargs={'encoding': 'utf-8'}
    )
    documents = loader.load()
    
    if not documents:
        print("Nessun documento Markdown trovato.")
        return []
        
    all_chunks = []
    # Chunking per intestazioni principali Markdown (più robusto)
    splitter = MarkdownHeaderTextSplitter(headers_to_split_on=["#", "##"])
    
    for doc in documents:
        try:
            chunks = splitter.split_text(doc.page_content)
            for chunk in chunks:
                # Puoi aggiungere come metadata il titolo del chunk se vuoi
                all_chunks.append(Document(page_content=chunk, metadata=doc.metadata))
        except Exception:
            # In caso di problemi fallback: tutto il file in un unico chunk
            all_chunks.append(doc)
            
    print(f"Totale chunk indicizzati: {len(all_chunks)}")
    return all_chunks