class ToDoList:
    def __init__(self):
        self.tasks = {}
    def add_task(self, task_name):
        """Add a new task to the list."""
        task_name = task_name.strip()
        if not task_name:
            print("Task name cannot be empty.")
            return
        if task_name.lower() not in (t.lower() for t in self.tasks):
            self.tasks[task_name] = False
            print(f"Task '{task_name}' added.")
        else:
            print(f"Task '{task_name}' already exists.")
    def remove_task(self, task_name):
        """Remove a task from the list."""
        task_name = task_name.strip()
        matching_task = None
        for t in self.tasks:
            if t.lower() == task_name.lower():
                matching_task = t
                break
        else:
            print(f"Task '{task_name}' not found.")
    def mark_task(self, task_name):
        """Mark a task as completed."""
        task_name = task_name.strip()
        matching_task = None
        for t in self.tasks:
            if t.lower() == task_name.lower():
                matching_task = t
                break
        if matching_task:
            if self.tasks[matching_task]:
                print(f"Task '{matching_task}' is already marked as completed.")
            else:
                self.tasks[matching_task] = True
                print(f"Task '{matching_task}' marked as completed.")
        else:
            print(f"Task '{task_name}' not found.")
    def view_tasks(self):
        """View all tasks in the list."""
        if not self.tasks:
            print("Your to-do list is empty.")
        else:
            print("To-Do List:")
            for task, completed in self.tasks.items():
                status = "✓ Completed" if completed else "✗ Not Completed"
                print(f" - {task}: {status}")
def main():
    todo_list = ToDoList()
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
            todo_list.add_task(task_name)
        elif choice == "2":
            task_name = input("Enter task name to remove: ")
            todo_list.remove_task(task_name)
        elif choice == "3":
            task_name = input("Enter task name to mark as completed: ")
            todo_list.mark_task(task_name)
        elif choice == "4":
            todo_list.view_tasks()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please choose a number from 1 to 5.")
if __name__ == "__main__":
    main()
