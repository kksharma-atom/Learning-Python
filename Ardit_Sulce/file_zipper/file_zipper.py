import FreeSimpleGUI as sg
from zip_creator import make_archive

label_for_files = sg.Text("Select files to compress: ")
label_for_folder = sg.Text("Select destination folder: ")

files_textbox = sg.InputText(disabled=True)
folder_textbox = sg.InputText(disabled=True)

fileSelection_button = sg.FilesBrowse("Choose", key="files")
folderSelection_button = sg.FolderBrowse("Choose", key="folder")

compress_button = sg.Button("Compress")

output_label = sg.Text(key="output")


window = sg.Window("File Zipper", 
                   layout=[[label_for_files, files_textbox, fileSelection_button ],
                           [label_for_folder, folder_textbox, folderSelection_button],
                           [compress_button, output_label]],
                           font=("Helvetica", 15))

while True:  
        event, values = window.read()
        # print(event, values)
        
        if event == sg.WIN_CLOSED:
            break
        elif event == "Compress" and values["files"]:
                filepaths = values["files"].split(";")
                folder = values["folder"]

                make_archive(filepaths, folder)
                window["output"].update(value="Compresssion successful!")

        

window.close()