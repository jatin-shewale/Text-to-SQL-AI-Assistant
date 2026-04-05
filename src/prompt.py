from langchain_core.prompts import ChatPromptTemplate

def get_prompt():
    return ChatPromptTemplate.from_template("""
You are a senior SQL expert.

Given the database schema:
{schema}

Convert the user question into SQL.

Rules:
- Only return SQL
- No explanation
- Use correct syntax

Question:
{question}
""")