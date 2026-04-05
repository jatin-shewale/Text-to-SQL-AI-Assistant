from langchain_ollama import ChatOllama
from langchain_core.output_parsers import StrOutputParser
from src.prompt import get_prompt
from src.config import MODEL_NAME

def get_sql_chain():

    llm = ChatOllama(
        model=MODEL_NAME,
        temperature=0
    )

    prompt = get_prompt()

    chain = prompt | llm | StrOutputParser()

    return chain