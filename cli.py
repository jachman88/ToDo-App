# This is a basic command line To-Do list app
import functions
import time
# Banner
print("*" * 10)
print("To Do List")
print("*" * 10)

now = time.strftime("%b %d, %Y %H:%M:%S")
print("It is", now)
while True:
    user_action = input('Type add, show, edit, delete or exit: ')
    user_action = user_action.strip()
    
    if user_action.startswith("add"):
        user_action = user_action[4:]

        my_list = functions.get_list()

        my_list.append(user_action)

        functions.write_list(my_list)


    elif user_action == 'show':
        my_list = functions.get_list()

        for task_number, item in enumerate(my_list):
            item = item.strip()
            row = f"{task_number + 1}. {item.capitalize()}"
            print(row)

    elif user_action == 'edit':
        my_list = functions.get_list()
        try:
            task_number = int(input("Which task would you like to edit? "))
            task_number = task_number - 1
            new_task = input("What would you like to do now? ")
            my_list[task_number] = new_task + '\n'

            functions.write_list(my_list)

        except ValueError:
            print("Invalid entry detected. Try again.")
            continue
        except IndexError:
            print("Invalid entry detected. Try again.")
            continue


    elif user_action == 'delete':

        number = int(input("Which task would you like to delete? "))

        my_list = functions.get_list()
        index = number - 1
        todo_to_remove = my_list[index].strip('\n')
        my_list.pop(number - 1)

        functions.write_list(my_list)

        print(f"{todo_to_remove.capitalize()} was removed from the list.")

    else:
        break

print("Good Bye!")  # Change messaging here once writing to file feature has been added.
# Add feature or note stating that the list has been saved to the disk.
