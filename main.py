from src.pipeline import run_pipeline

while True:
    question = input("Ask: ")

    sql, result = run_pipeline(question)

    print("\nSQL:", sql)
    print("Result:", result)
    print("-" * 40)