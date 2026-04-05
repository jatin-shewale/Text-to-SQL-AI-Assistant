def execute_query(db, query):
    try:
        result = db.run(query)
        return result
    except Exception as e:
        return f"Error: {e}"