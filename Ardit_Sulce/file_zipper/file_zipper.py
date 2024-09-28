import FreeSimpleGUI as sg

label_for_files = sg.Text("Select files to compress: ")
label_for_folder = sg.Text("Select destination folder: ")

files_textbox = sg.InputText(disabled=True)
folder_textbox = sg.InputText(disabled=True)

fileSelection_button = sg.FilesBrowse("Choose")
folderSelection_button = sg.FolderBrowse("Choose")

compress_button = sg.Button("Compress")


window = sg.Window("File Zipper", 
                   layout=[[label_for_files, files_textbox, fileSelection_button ],
                           [label_for_folder, folder_textbox, folderSelection_button],
                           [compress_button]])
window.read()
window.close() 