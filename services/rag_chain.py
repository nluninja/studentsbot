"""RAG chain implementation for question-answering."""

from typing import Dict, Any, List, Optional

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_community.vectorstores import FAISS

from config.settings import Config


class RAGChainManager:
    """Manages the RAG (Retrieval-Augmented Generation) chain."""
    
    def __init__(self, vectorstore: FAISS, config: Config = None):
        self.config = config or Config()
        self.vectorstore = vectorstore
        self.llm = ChatGoogleGenerativeAI(
            model=self.config.MODEL_NAME_LLM,
            temperature=self.config.TEMPERATURE,
            convert_system_message_to_human=False
        )
        self.retriever = vectorstore.as_retriever(
            search_kwargs={"k": self.config.RETRIEVER_K}
        )
        self.chain = self._create_chain()
    
    def _create_chain(self):
        """Create the RAG chain."""
        prompt = ChatPromptTemplate.from_messages([
            ("system", self.config.get_system_prompt()),
            MessagesPlaceholder(variable_name="chat_history"),
            ("human", "{input}"),
        ])
        
        question_answer_chain = create_stuff_documents_chain(self.llm, prompt)
        
        def custom_chain(input_data: Dict[str, Any]) -> Dict[str, Any]:
            query = input_data["input"]
            chat_history = input_data.get("chat_history", [])
            docs = self.retriever.invoke(query)
            
            # Debug output
            print(query)
            for i, doc in enumerate(docs):
                print(f"Document {i + 1}:")
                print("Metadata:", doc.metadata)
                print("-" * 40)
            
            output = question_answer_chain.invoke({
                "input": query,
                "context": docs,
                "chat_history": chat_history
            })
            
            if isinstance(output, dict):
                return output
            else:
                return {"answer": output}
        
        return custom_chain
    
    def invoke(self, query: str, chat_history: List = None) -> Dict[str, Any]:
        """Invoke the RAG chain with a query."""
        return self.chain({
            "input": query,
            "chat_history": chat_history or []
        })