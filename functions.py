def get_list(filename='todos.txt'):
    """
    Function that returns a file as a list.
    """
    with open(filename, 'r') as file_local:
        my_list_local = file_local.readlines()
    return my_list_local

def write_list(todo_list, filename='todos.txt'):
    """
    Writes list to file
    """
    with open(filename, 'w') as file_local:
        file_local.writelines(todo_list)