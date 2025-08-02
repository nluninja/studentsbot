"""Refactored StudentsBot application entry point."""

from dotenv import load_dotenv
from langchain.globals import set_verbose

from studentsbot import StudentsBot
from config.settings import Config

set_verbose(True)


def main_chat():
    """Main chat function with refactored architecture."""
    bot = StudentsBot()
    
    recreate = input("Rigenerare vectorstore? (s/N): ").lower() == 's'
    if not bot.initialize(force_recreate_vectorstore=recreate):
        print("Errore durante l'inizializzazione del bot.")
        return
    
    bot.run_interactive()


if __name__ == "__main__":
    load_dotenv()
    main_chat()