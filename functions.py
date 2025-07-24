def get_todos():
    with open("todos.txt",'r') as file:
        localtodos=file.readlines()
    return localtodos


def updatetodos(updatedtodo):
    with open("todos.txt",'w') as file:
        file.writelines(updatedtodo)