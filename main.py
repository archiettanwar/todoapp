import FreeSimpleGUI as gu
import functions

label=gu.Text("type a todo")
input_box=gu.InputText(tooltip="Enter a todo",key="todo")
add_button=gu.Button("ADD")
list_of_todos=gu.Listbox(values=functions.get_todos(),key='todos',enable_events=True,size=[30,10])
edit_button=gu.Button("EDIT")

window=gu.Window("ToDo App",
                 layout=[[label],[input_box,add_button],[list_of_todos,edit_button]]
                 ,font=('Serif',10))


while True:
    event,values=window.read()
    print(event)
    print(values)
    match event:
        case 'ADD':
            todos=functions.get_todos()
            newtodo=values['todo']+'\n'
            todos.append(newtodo)
            functions.updatetodos(todos)
            window['todos'].update(values=todos)
        case 'EDIT':
            todo_to_edit=values['todos'][0]
            new_todo=values['todo']+'\n'
            todos=functions.get_todos()
            index=todos.index(todo_to_edit)
            todos[index]=new_todo
            functions.updatetodos(todos)
            window['todos'].update(values=todos)
        case 'todos':
            window['todo'].update(value=values['todos'][0])
        case gu.WIN_CLOSED:
            break

window.close()

