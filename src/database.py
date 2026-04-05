from langchain_community.utilities import SQLDatabase
from src.config import DB_URI

def get_database():
    return SQLDatabase.from_uri(DB_URI)