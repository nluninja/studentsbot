"""Logging utilities for the application."""

import logging
import sys
from typing import Optional


class Logger:
    """Application logger with consistent formatting."""
    
    def __init__(self, name: str = "studentsbot", level: int = logging.INFO):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(level)
        
        if not self.logger.handlers:
            handler = logging.StreamHandler(sys.stdout)
            formatter = logging.Formatter(
                '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
            )
            handler.setFormatter(formatter)
            self.logger.addHandler(handler)
    
    def info(self, message: str):
        """Log info message."""
        self.logger.info(message)
    
    def error(self, message: str, exc_info: bool = False):
        """Log error message."""
        self.logger.error(message, exc_info=exc_info)
    
    def warning(self, message: str):
        """Log warning message."""
        self.logger.warning(message)
    
    def debug(self, message: str):
        """Log debug message."""
        self.logger.debug(message)


def get_logger(name: Optional[str] = None) -> Logger:
    """Get a logger instance."""
    return Logger(name or "studentsbot")