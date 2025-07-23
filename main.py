import FreeSimpleGUI as gu
import functions

label=gu.Text("type a todo")
input_box=gu.InputText(tooltip="Enter a todo")
add_button=gu.Button("ADD")

window=gu.Window("ToDo App",layout=[[label],[input_box,add_button]])
window.read()
window.close()

