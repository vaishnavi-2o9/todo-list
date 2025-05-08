import sqlite3
from todo_db import ToDoList
class ToDoListDB(ToDoList):
    def __init__(self, db_name):
        super().__init__()
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY,
                task_name TEXT NOT NULL,
                completed INTEGER NOT NULL DEFAULT 0
            )
        """)
        self.conn.commit()
    def add_task(self, task_name):
        try:
            task_name = task_name.strip()
            if not task_name:
                print("Task name cannot be empty.")
                return
            self.cursor.execute("SELECT * FROM tasks WHERE task_name = ?", (task_name,))
            if self.cursor.fetchone():
                print(f"Task '{task_name}' already exists.")
            else:
                self.cursor.execute("INSERT INTO tasks (task_name, completed) VALUES (?, 0)", (task_name,))
                self.conn.commit()
                print(f"Task '{task_name}' added.")
        except sqlite3.Error as e:
            print(f"An error occurred: {e}")
    def remove_task(self, task_name):
    
        try:
            task_name = task_name.strip()
            self.cursor.execute("SELECT * FROM tasks WHERE task_name = ?", (task_name,))
            if self.cursor.fetchone():
                self.cursor.execute("DELETE FROM tasks WHERE task_name = ?", (task_name,))
                self.conn.commit()
                print(f"Task '{task_name}' removed.")
            else:
                print(f"Task '{task_name}' not found.")
        except sqlite3.Error as e:
            print(f"An error occurred: {e}")
    def mark_task(self, task_name):
        try:
            task_name = task_name.strip()
            self.cursor.execute("SELECT * FROM tasks WHERE task_name = ?", (task_name,))
            if self.cursor.fetchone():
                self.cursor.execute("UPDATE tasks SET completed = 1 WHERE task_name = ?", (task_name,))
                self.conn.commit()
                print(f"Task '{task_name}' marked as completed.")
            else:
                print(f"Task '{task_name}' not found.")
        except sqlite3.Error as e:
            print(f"An error occurred: {e}")
    def view_tasks(self):
         
        try:
            self.cursor.execute("SELECT * FROM tasks")
            tasks = self.cursor.fetchall()
            if not tasks:
                print("Your to-do list is empty.")
            else:
                print("To-Do List:")
                for task in tasks:
                    status = "✓ Completed" if task[2] else "✗ Not Completed"
                    print(f" - {task[1]}: {status}")
        except sqlite3.Error as e:
            print(f"An error occurred: {e}")
    def close_connection(self):
        self.conn.close()
def main():
    db_name = "todo_db.db"
    todo_list_db = ToDoListDB(db_name)
    while True:
        print("\nOptions:")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. Mark Task as Completed")
        print("4. View Tasks")
        print("5. Quit")
        
        choice = input("Choose an option (1-5): ").strip()
        if choice == "1":
            task_name = input("Enter task name: ")
            todo_list_db.add_task(task_name)
        elif choice == "2":
            task_name = input("Enter task name to remove: ")
            todo_list_db.remove_task(task_name)
        elif choice == "3":
            task_name = input("Enter task name to mark as completed: ")
            todo_list_db.mark_task(task_name)
        elif choice == "4":
             todo_list_db.view_tasks()
        elif choice == "5":
            print("Goodbye!")
            todo_list_db.close_connection()
            break
        else:
            print("Invalid option. Please choose a number from 1 to 5.")
if __name__ == "__main__":
    main()