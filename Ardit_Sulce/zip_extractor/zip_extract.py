import FreeSimpleGUI as sg
from extract_mod import unpzip_contents

sg.theme("Black")

label_select_archive_file = sg.Text("Select archive:", size=15)
filepath_display_textbox = sg.InputText()
filepath_select_button = sg.FileBrowse("Choose", key="filepath")

label_select_dest_dir = sg.Text("Select destination:", size=15)
dest_dir_display_textbox = sg.InputText()
dest_dir_select_button = sg.FolderBrowse("Choose", key="dest_folder")

extract_button = sg.Button("Extract", key="extract")

result_label = sg.Text(key="result")

window = sg.Window("Archive Extractor", 
                   layout=[[label_select_archive_file,
                            filepath_display_textbox,
                            filepath_select_button],
                           [label_select_dest_dir,
                            dest_dir_display_textbox,
                            dest_dir_select_button],
                            [extract_button, result_label]],
                            font=("Helvetica", 13))



while True:
    event, values = window.read()
    print(event)
    print(values)
    match event:
        case "extract":
            unpzip_contents(values["filepath"], values["dest_folder"])
            window["result"].update(value="Files extracted to the specified folder")

        case sg.WIN_CLOSED:
            break

window.close()      


