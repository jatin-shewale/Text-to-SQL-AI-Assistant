import sqlite3

conn = sqlite3.connect("data/student_grades.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS grades (
    id INTEGER PRIMARY KEY,
    name TEXT,
    subject TEXT,
    score INTEGER,
    grade TEXT
)
""")

data = [
    (1, "Aman", "Math", 95, "A"),
    (2, "Anshu", "Math", 78, "C"),
    (3, "Akshu", "History", 88, "B"),
    (4, "Rahul", "History", 92, "A"),
    (5, "Divyansh", "Science", 85, "B"),
    (6, "Nandini", "Math", 65, "D")
]

cursor.executemany("INSERT OR IGNORE INTO grades VALUES (?, ?, ?, ?, ?)", data)

conn.commit()
conn.close()

print("Database created ✅")