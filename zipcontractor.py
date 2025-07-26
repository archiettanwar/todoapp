from zip_convertor import zip_convertor
import FreeSimpleGUI as sg

label1=sg.Text("enter files to compress")
input1=sg.Input()
button1=sg.FilesBrowse("choose",key="filepaths")

label2=sg.Text("enter directory to put zip file")
input2=sg.Input()
button2=sg.FolderBrowse("choose",key="folder")

convertbu=sg.Button("Convert")
output_label=sg.Text(key='output',text_color='green')

layout=[[label1,input1,button1],
        [label2,input2,button2],
        [convertbu,output_label]]

window=sg.Window("File Compressor",layout=layout)

while True:
    event,values=window.read()
    filepaths=values['filepaths'].split(';')
    folder=values['folder']
    zip_convertor(filepaths,folder)
    window['output'].update(value="Compression complete")

window.close()