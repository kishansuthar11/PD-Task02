class ToDoMaNager:
    def __init__(self, filename='ToDo.txt'):
        self.filename = filename
    
    def read_tasks(self):
        try:
            with open(self.filename, 'r') as f:
                return f.read().splitlines()
        except:
            return []    
            
    def write_tasks(self, tasks):
        with open(self.filename, 'w') as f:
            for task in tasks:
                f.write(task + '\n')
    
    def add_task(self):
        task = input("Enter the task to add: ")
        tasks = self.read_tasks()
        tasks.append(task)
        self.write_tasks(tasks)
        print(f"Task '{task}' added successfully.")             
        
    def remove_task(self):
        tasks = self.read_tasks()
        if not tasks:
            print("No tasks to remove.")
            return
        self.view_tasks()
        try:
            index = int(input("Enter the task number to remove: "))
            if 0 <= index <= len(tasks):
                removed_task = tasks.pop(index-1)
                self.write_tasks(tasks)
                print(f"Task '{removed_task}' removed successfully.")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            
    def view_tasks(self):
        tasks = self.read_tasks()
        if not tasks:
            print("No tasks available.")
        else:
            print("Current Tasks:")
            for i, task in enumerate(tasks, 1):
                print(f"{i}. {task}")
            print()
            
    def run(self):
        print("Welcome to To-Do Manager")
        while True:
            print("\n--- To-Do Manager Menu ---")
            print("1. Add Task")
            print("2. Remove Task")
            print("3. View Tasks")
            print("4. Exit")
            choice = input("choose option (1-4): ")
            if choice == '1':
                self.add_task()
            elif choice == '2':
                self.remove_task()
            elif choice == '3':
                self.view_tasks()
            elif choice == '4':            
                print("Exiting To-Do Manager. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")
                
if __name__ == "__main__":
    todo_manager = ToDoMaNager()
    todo_manager.run()  