"""Main StudentsBot application class."""

from typing import Optional
from langchain_community.chat_message_histories import ChatMessageHistory

from config.settings import Config
from services.vectorstore_manager import VectorStoreManager
from services.rag_chain import RAGChainManager
from utils.logger import get_logger
from utils.exceptions import StudentsBotError, VectorStoreError, RAGChainError


class StudentsBot:
    """Main application class for the StudentsBot."""
    
    def __init__(self, config: Optional[Config] = None):
        self.config = config or Config()
        self.logger = get_logger("StudentsBot")
        self.vectorstore_manager = VectorStoreManager(self.config)
        self.rag_chain_manager: Optional[RAGChainManager] = None
        self.chat_history = ChatMessageHistory()
    
    def initialize(self, force_recreate_vectorstore: bool = False) -> bool:
        """Initialize the bot with vector store and RAG chain."""
        try:
            self.logger.info("Inizializzazione chatbot...")
            
            # Initialize vector store
            vectorstore = self.vectorstore_manager.get_vectorstore(force_recreate_vectorstore)
            if not vectorstore:
                raise VectorStoreError("Errore nella creazione del vectorstore.")
            
            # Initialize RAG chain
            self.rag_chain_manager = RAGChainManager(vectorstore, self.config)
            if not self.rag_chain_manager:
                raise RAGChainError("Errore interno: la catena RAG non è inizializzata!")
            
            self.logger.info("Inizializzazione completata con successo.")
            return True
            
        except Exception as e:
            self.logger.error(f"Errore durante l'inizializzazione: {e}", exc_info=True)
            return False
    
    def ask(self, query: str) -> str:
        """Ask a question to the bot."""
        if not self.rag_chain_manager:
            raise RAGChainError("Bot non inizializzato. Chiamare initialize() prima.")
        
        try:
            response = self.rag_chain_manager.invoke(query, self.chat_history.messages)
            answer = response.get("answer", "Non ho trovato una risposta.")
            
            # Update chat history
            self.chat_history.add_user_message(query)
            self.chat_history.add_ai_message(answer)
            
            return answer
            
        except Exception as e:
            error_msg = f"Errore durante l'elaborazione della query: {e}"
            self.logger.error(error_msg, exc_info=True)
            return error_msg
    
    def clear_history(self):
        """Clear chat history."""
        self.chat_history = ChatMessageHistory()
        self.logger.info("Cronologia chat cancellata.")
    
    def run_interactive(self):
        """Run the bot in interactive mode."""
        if not self.rag_chain_manager:
            print("Errore: Bot non inizializzato.")
            return
        
        print("\nChatbot pronta. Scrivi 'esci' per terminare.")
        print("----------------------------------------------------")
        
        while True:
            try:
                query = input("Tu: ")
                if query.lower() in self.config.EXIT_COMMANDS:
                    print("Chatbot: Arrivederci!")
                    break
                
                if not query.strip():
                    continue
                
                print("Chatbot: Sto pensando...")
                answer = self.ask(query)
                print(f"Chatbot: {answer}\n")
                
            except KeyboardInterrupt:
                print("\nChatbot: Arrivederci!")
                break
            except Exception as e:
                self.logger.error(f"Errore nell'interfaccia interattiva: {e}", exc_info=True)
                print(f"Errore: {e}")
            
            print("----------------------------------------------------")