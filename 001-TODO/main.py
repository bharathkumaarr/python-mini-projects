
decor = '--------------------------------------------------'
from tasks_functions import add_tasks, delete_tasks, list_tasks
    

if __name__ == '__main__':
    print('Welcome to our To-Do List App :)')
    while True:
        print('Please select any of the following:')
        print(decor)
        print('''
        1. Add a Task
        2. Delete a Task
        3. List all the Tasks
        4. Exit
        ''')
        print(decor)
        try:
            user_choice = int(input("Enter the # you'd like to choose: "))
            if user_choice == 1:
                add_tasks()
            elif user_choice == 2:
                delete_tasks()
            elif user_choice == 3:
                list_tasks()
            elif user_choice == 4:
                print('Goodbye 👋👋')
                break
            else:
                print('Invalid Input. Try again!')
        except ValueError:
            print('Invalid input. Please enter a number.')