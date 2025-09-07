import sqlite3

# Connect to SQLite database (creates if not exists)
conn = sqlite3.connect("tasks.db", check_same_thread=False)
c = conn.cursor()

# Create tasks table if not exists
c.execute("""CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    task TEXT NOT NULL
)""")
conn.commit()

# Function to add a task
def add_task(task):
    c.execute("INSERT INTO tasks (task) VALUES (?)", (task,))
    conn.commit()

# Function to get all tasks
def get_tasks():
    c.execute("SELECT * FROM tasks")
    return c.fetchall()

# Function to delete a task
def delete_task(task_id):
    c.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
    conn.commit()
