import FreeSimpleGUI as gu
import functions
import time

gu.theme('Black')
clock=gu.Text('',key='clock',text_color='orange')
label=gu.Text("type a todo")
input_box=gu.InputText(tooltip="Enter a todo",key="todo")
add_button=gu.Button("ADD")
list_of_todos=gu.Listbox(values=functions.get_todos(),
                         key='todos',
                         enable_events=True,size=[45,10])
edit_button=gu.Button("EDIT")
comp_button=gu.Button("COMPLETE")
exit_button=gu.Button("EXIT")


window=gu.Window("ToDo App",
                 layout=[[clock],[label],
                         [input_box,add_button],
                         [list_of_todos],
                         [edit_button,comp_button,exit_button]]
                 ,font=('Serif',10))
while True:
    event,values=window.read(timeout=200)
    window['clock'].update(value=time.strftime('%d-%m-%Y,%H:%M:%S %p'))
    match event:
        case 'ADD':
            todos=functions.get_todos()
            newtodo=values['todo']+'\n'
            todos.append(newtodo)
            functions.updatetodos(todos)
            window['todos'].update(values=todos)
            window['todo'].update(value='')
        case 'EDIT':
            try:
                todo_to_edit=values['todos'][0]
                new_todo=values['todo']+'\n'
                todos=functions.get_todos()
                index=todos.index(todo_to_edit)
                todos[index]=new_todo
                functions.updatetodos(todos)
                window['todos'].update(values=todos)
            except IndexError:
                gu.popup("Please select a to-do first",font=('Helvetica',20))
        case 'COMPLETE':
            try:
                todo_to_remove=values['todos'][0]
                todos=functions.get_todos()
                index=todos.index(todo_to_remove)
                todos.pop(index)
                functions.updatetodos(todos)
                window['todos'].update(values=todos)
                window['todo'].update(value='')
            except IndexError:
                gu.popup("Please choose a todo first",font=('Helvetica',20))
        case 'EXIT':
            break
        case 'todos':
            window['todo'].update(value=values['todos'][0])
        case gu.WIN_CLOSED:
            break

window.close()