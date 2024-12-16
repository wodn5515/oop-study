class TodoList:
    def __init__(self, owner):
        self.owner = owner
        self.todos = []

    def __repr__(self):
        return f"{self.owner}'s ToDo"

    def add(self, task):
        self.todos.append(task)

    def list(self):
        for idx, task in enumerate(self.todos, 1):
            print(f"{idx} | {task}")

    def update(self, idx: int, task: str):
        self.todos[idx-1] = task

    def remove(self, idx):
        del self.todos[idx-1]


class TodoManager:
    def __init__(self):
        self.todoslist = {}

    def get_todos(self):
        while True:
            try:
                owner = input("Enter Owner's name: ")
                todos = self.todoslist[owner]
            except KeyError:
                print(f"Cannot find {owner}. Check owner's name")
            else:
                print(f"Successfully get todos({owner})")
                break
        return todos

    def create_todos(self):
        owner = input("Enter Owner's name: ")
        todos = TodoList(owner=owner)
        self.todoslist[owner] = todos
        print(f"Successfully create todos({owner})")
        return todos
    
    def run(self):
        todos = self.create_todos()
        self.action(todos)

    def action(self, todos: TodoList):
        while True:
            command = input(f"[{todos}]Enter command (add, list, update, remove, exit)")
            if command == "add":
                task = input("Enter task: ")
                todos.add(task)
            elif command == "list":
                todos.list()
            elif command == "update":
                idx, task = input("Enter the task number and new task (split with '|'): ").split("|")
                todos.update(int(idx), task)
            elif command == "remove":
                idx = int(input("Enter the task number to remove: "))
                todos.remove(idx)
            elif command == "exit":
                exit_command = input("1) Exit\n2) Change todos\n3) Create todos\nChoose number: ")
                if exit_command == "1":
                    break
                elif exit_command == "2":
                    todos = self.get_todos()
                elif exit_command == "3":
                    todos = self.create_todos()
                else:
                    print("Unknown command!")
            else:
                print("Unknown command!")


if __name__ == "__main__":
    manager = TodoManager()
    manager.run()

