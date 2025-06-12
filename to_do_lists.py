from time import sleep

tasks = {}

def add_task(new_task):
    task_id = max(tasks.keys(), default=0) + 1 # Having default will prevent the error in tasks dictionary which causes error if empty
    tasks[task_id] = new_task
    print("Task added successfully.\nUpdated list:")
    for key, value in tasks.items():
        print(f"{key}. {value}")
    sleep(len(tasks) + 1) # This give time for user to read base on the amount of list

def remove_task(task_to_remove):
    global tasks #Declare as global first so you tell to Python that you're updating the tasks = {} on line 3 rather than creating new dictionary
    try:
        tasks.pop(task_to_remove)
        # Re-index
        tasks = {i+1: task for i, task in enumerate(tasks.values())}
        print("Task removed successfully.\nUpdated list:")
        
        # Showing the re-indexed dictionary
        for key, value in tasks.items():
            print(f"{key}. {value}")
    except KeyError:
        print("Task number not found.")
    sleep(len(tasks) + 1) # This give time for user to read base on the amount of list

def view_task():
    if not tasks:
        print("No tasks yet.")
    else:   
        print("Current lists:")
        for key,value in tasks.items():
            print(f"{key}. {value}")
        sleep(len(tasks) + 1) # This give time for user to read base on the amount of list

def main():
    while True:
        print("------------------------------------")
        print("Welcome to to-do-list.\nEnter a function:")
        print("1 - Add task")
        print("2 - Remove task")
        print("3 - View task/s")
        print("4 - quit")
        print("------------------------------------")
        try:
            user_input = int(input("Enter a function: "))
            print("------------------------------------")
            match user_input:
                case 1:
                    new_task = input("Enter a task: ")
                    add_task(new_task)
                case 2:
                    if not tasks:
                        print("No tasks to remove.")
                    else:
                        for key, value in tasks.items():
                            print(f"{key}. {value}")
                        task_to_remove = int(input("Enter task number to remove: "))
                        remove_task(task_to_remove)
                case 3:
                    view_task()
                case 4:
                    print("Goodbye!")
                    break
                case _:
                    print("Out of scope")
        except ValueError:
            print("Enter a number only.")
        except KeyError:
            print("Not existing.")

if __name__ == '__main__':
    main()