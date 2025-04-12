tasks = ["Gym", "Study", "Laundry"]


def display_menu():
    print("\nToDo List Application")
    print("1: Add Task")
    print("2: View Tasks")
    print("3: Delete Task")
    print("4: Exit")


def add_task():
    task = input("What task would you like to add to your list? \n")
    tasks.append(task)
    print(f"'{task}' has been added to the list\n")


def view_tasks():
    print("Here are your current tasks in your to do list: \n")
    for i in range(len(tasks)):
        print(f"{i + 1}: {tasks[i]}")


def delete_task():
    view_tasks()
    if tasks:
        try:
            tasknum = int(input("Enter the task number to delete: ")) - 1
            if 0 <= tasknum < len(tasks):
                removed_task = tasks.pop(tasknum)
                print(f"Task '{removed_task}' deleted successfully.")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def main():

    while True:

        display_menu()
        choice = input("What would you like to do? ")

        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            delete_task()
        elif choice == "4":
            break
        else:
            print("Invalid input, try again")


main()
