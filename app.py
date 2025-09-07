import streamlit as st
import sqlite3
import random

# -----------------------
# Database setup
# -----------------------
conn = sqlite3.connect("tasks.db", check_same_thread=False)
c = conn.cursor()
c.execute("""
CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    task TEXT NOT NULL
)
""")
conn.commit()

# -----------------------
# Database functions
# -----------------------
def add_task(task):
    c.execute("INSERT INTO tasks (task) VALUES (?)", (task,))
    conn.commit()

def get_tasks():
    c.execute("SELECT * FROM tasks")
    return c.fetchall()

def update_task(task_id, new_task):
    c.execute("UPDATE tasks SET task = ? WHERE id = ?", (new_task, task_id))
    conn.commit()

def delete_task(task_id):
    c.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
    conn.commit()

# -----------------------
# Streamlit UI
# -----------------------
st.title("📝 To-Do App")

# -----------------------
# Initialize session state
# -----------------------
if "edit_task" not in st.session_state:
    st.session_state.edit_task = {}  # Tracks which task is in edit mode

# -----------------------
# Add Task Form
# -----------------------
with st.form("add_task_form", clear_on_submit=True):
    task_input = st.text_input("Enter a new task")
    submitted = st.form_submit_button("➕ Add Task")
    if submitted:
        if task_input.strip():
            add_task(task_input.strip())
            st.success(f"Task added: {task_input.strip()}")
            st.rerun()  # Refresh immediately
        else:
            st.warning("Please enter a task!")

# -----------------------
# AI Mock Task Button
# -----------------------
if st.button("🤖 Auto-Generate Task"):
    mock_tasks = [
        "Read a book chapter",
        "Practice yoga for 10 minutes",
        "Write a journal entry",
        "Organize desk",
        "Drink water 2 glasses",
        "Go for a 15-minute walk"
    ]
    ai_task = random.choice(mock_tasks)
    add_task(ai_task)
    st.success(f"AI suggested and added: {ai_task}")
    st.rerun()  # Refresh immediately

# -----------------------
# Display Tasks
# -----------------------
st.subheader("📌 Your Tasks")

tasks = get_tasks()

for task_id, task_text in tasks:
    col_task, col_edit, col_delete = st.columns([5, 1, 1])

    # Edit mode
    if st.session_state.edit_task.get(task_id, False):
        new_task_text = col_task.text_input(
            "Update Task:", value=task_text, key=f"edit_input_{task_id}"
        )
        if col_edit.button("✅ Save", key=f"save_{task_id}"):
            if new_task_text.strip():
                update_task(task_id, new_task_text.strip())
                st.success("Task updated successfully!")
                st.session_state.edit_task[task_id] = False
                st.rerun()  # Refresh immediately after save
            else:
                st.warning("Task cannot be empty!")
    else:
        col_task.write(task_text)
        if col_edit.button("✏️", key=f"editbtn_{task_id}"):
            st.session_state.edit_task[task_id] = True
            st.rerun()  # Refresh immediately to show input box

    # Delete button
    if col_delete.button("❌", key=f"del_{task_id}"):
        delete_task(task_id)
        st.success("Task deleted successfully!")
        st.rerun()  # Refresh immediately after delete

if not tasks:
    st.info("No tasks yet. Add one above!")
