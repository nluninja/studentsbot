"""Custom exceptions for the StudentsBot application."""


class StudentsBotError(Exception):
    """Base exception for StudentsBot application."""
    pass


class VectorStoreError(StudentsBotError):
    """Exception raised for vector store related errors."""
    pass


class DocumentLoadError(StudentsBotError):
    """Exception raised when document loading fails."""
    pass


class RAGChainError(StudentsBotError):
    """Exception raised for RAG chain related errors."""
    pass


class ConfigurationError(StudentsBotError):
    """Exception raised for configuration related errors."""
    pass