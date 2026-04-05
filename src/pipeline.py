from src.database import get_database
from src.agents.sql_generator import get_sql_chain
from src.agents.sql_executor import execute_query

def run_pipeline(question):

    db = get_database()
    schema = db.get_table_info()

    chain = get_sql_chain()

    sql_query = chain.invoke({
        "schema": schema,
        "question": question
    }).strip()

    result = execute_query(db, sql_query)

    return sql_query, result