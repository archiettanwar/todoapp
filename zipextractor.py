import FreeSimpleGUI as sg
from zip_extractor import zipextractor

label1=sg.Text("choose directory to extract from ",justification='left')
input1=sg.Input(tooltip="enter location of directory",justification='right')
button1=sg.FileBrowse("choose",key="to extract from")
label2=sg.Text("chose directory to extract",justification='left')
input2=sg.Input(tooltip="enter directory",justification='right')
button2=sg.FolderBrowse("Choose",key="to extract")
button3=sg.Button("Extract",mouseover_colors="green",key="extract")
output_text=sg.Text("",text_color="green",key='output')

layout=[[label1,input1,button1],
        [label2,input2,button2],
        [button3,output_text]]

window=sg.Window("ZIP EXTRACTOR 7000",layout=layout)

while True:
    event,values=window.read(timeout=1000)
    match event:
        case 'extract':
            fromdir=values['to extract from']
            todir=values['to extract']
            zipextractor(fromdir,todir)
            window['output'].update(value='Extraced!')
        case sg.WIN_CLOSED:
            break
window.close()