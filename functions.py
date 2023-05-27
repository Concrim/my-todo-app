def get_todos(filepath='todos.txt'):
    """This is used to obtain the todos from a list (file)"""
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath='todos.txt'):
    """This is used to write the todos in a list (file) """
    with open(filepath, 'w') as file_local:
        file_local.writelines(todos_arg)
