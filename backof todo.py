import functions
while True:
    user_input=input("add / show / edit / complete / exit :")
    user_in=user_input.strip()
    if 'add' in user_in:
        newtodo=user_input[4:]+'\n'
        todos=functions.get_todos()
        todos.append(newtodo)
        functions.updatetodos(todos)
    elif 'show' in user_in:
        todos=functions.get_todos()
        for i,j in enumerate(todos):
            j=j.strip('\n')
            res=f"{i+1}~{j}"
            print(res)
    elif 'edit' in user_in:
            try:
                  todotoedit=int(user_input[5:])
                  todotoedit=todotoedit-1 
                  todos=functions.get_todos()
                  newtodo=input("enter new todo: ")+'\n'
                  todos[todotoedit]=newtodo
                  functions.updatetodos(todos)
            except (IndexError,ValueError) as e:
                 if e==IndexError:
                      print("wrong index")
                 elif e==ValueError:
                      print("wrong value given")
    elif 'complete' in user_in:
            try:
                  completed_todo=int(user_input[9:])
                  completed_todo=completed_todo-1
                  todos=functions.get_todos()
                  res=todos[completed_todo]
                  res=res.strip('\n')
                  todos.pop(completed_todo)
                  functions.updatetodos(todos)
                  print(f"{res} was removed from the list.")
            except IndexError:
                 print("there are not many tasks")
    elif 'exit' in user_input:
        print("Thanks")
        break
    else:
        print("Invalid input") 