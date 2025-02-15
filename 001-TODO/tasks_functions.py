tasks=[]
decor = '--------------------------------------------------'
def add_tasks():
    while True:
        task = input('Enter the task you want to add: ')
        tasks.append(task)
        print(f"Your task '{task}' has been added.")
        print()
        y_n = input('Do you want to add one more task? (y/n): ').lower()
        if y_n == 'y':
            continue
        elif y_n == 'n':
            return
        else:
            print("Invalid input. Please enter 'y' or 'n'.")
def delete_tasks():
    list_tasks()
    if tasks:
        try:
            del_choice = int(input('Choose the task # you want to delete (make sure it is a number): ')) - 1
            if 0 <= del_choice < len(tasks):
                del tasks[del_choice]
                print(f"Task number {del_choice + 1} has been deleted.")
            else:
                print('Invalid input. Task number out of range.')
        except ValueError:
            print('Invalid input. Please enter a number.')
    else:
        print("No tasks available to delete.")
    list_tasks()
    
def list_tasks():
    print(decor)
    if tasks:
        print("Here are all the tasks you've got:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")
    else:
        print("No tasks in the list.")
    print(decor)