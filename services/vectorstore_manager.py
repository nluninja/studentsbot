"""Vector store management for document retrieval."""

import os
import shutil
import time
from typing import Optional

from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import FAISS

from config.settings import Config
from utils.document_parser import load_and_split_documents


class VectorStoreManager:
    """Manages FAISS vector store operations."""
    
    def __init__(self, config: Config = None):
        self.config = config or Config()
        self.embeddings = GoogleGenerativeAIEmbeddings(
            model=self.config.MODEL_NAME_EMBEDDINGS
        )
    
    def get_vectorstore(self, force_recreate: bool = False) -> Optional[FAISS]:
        """Get or create vector store."""
        if os.path.exists(self.config.VECTORSTORE_PATH) and not force_recreate:
            try:
                print("Carico il vectorstore esistente...")
                return FAISS.load_local(
                    self.config.VECTORSTORE_PATH, 
                    self.embeddings, 
                    allow_dangerous_deserialization=True
                )
            except Exception as e:
                print(f"Errore caricamento vectorstore: {e}, lo rigenero...")
                shutil.rmtree(self.config.VECTORSTORE_PATH)
        
        return self._create_vectorstore()
    
    def _create_vectorstore(self) -> Optional[FAISS]:
        """Create new vector store from documents."""
        documents = load_and_split_documents(self.config.MARKDOWN_DIR)
        if not documents:
            print("Nessun documento da indicizzare.")
            return None
        
        batches = [
            documents[i:i + self.config.BATCH_SIZE] 
            for i in range(0, len(documents), self.config.BATCH_SIZE)
        ]
        
        vs = None
        for i, batch in enumerate(batches):
            print(f"Indicizzazione batch {i+1}/{len(batches)} ({len(batch)} doc)")
            batch_vs = FAISS.from_documents(batch, self.embeddings)
            
            if vs is None:
                vs = batch_vs
            else:
                vs.merge_from(batch_vs)
            
            if i < len(batches) - 1:
                print(f"Attendo {self.config.BATCH_WAIT} secondi per evitare rate limit...")
                time.sleep(self.config.BATCH_WAIT)
        
        if vs is None:
            print("Errore: vectorstore non creato.")
            return None
        
        print("Indicizzazione completata, salvo e ritorno il vectorstore!")
        vs.save_local(self.config.VECTORSTORE_PATH)
        return vs