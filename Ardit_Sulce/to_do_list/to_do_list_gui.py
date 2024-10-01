import functions
import FreeSimpleGUI as sg
import time
import os

if not os.path.exists("todos.txt"):
    with open("todos.txt", "w") as file:
        pass

sg.theme("Black")

clock = sg.Text("", key="clock")
label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter todo", key="todo")
add_button = sg.Button(key="Add", 
                       image_source="add.png", 
                       mouseover_colors="LightBlue2", 
                       tooltip="Add a To-Do item")
list_box = sg.Listbox(values=functions.get_todos(), key="todos",  
                      enable_events=True, size=[45, 10])
edit_button = sg.Button("Edit")

complete_button = sg.Button(key="Complete", 
                       image_source="complete.png", 
                       mouseover_colors="LightBlue2", 
                       tooltip="On To-Do completion")

exit_buttton = sg.Button("Exit")

window = sg.Window("My To-Do App", 
                  layout=[[clock],
                          [label],
                          [input_box],
                          [list_box],
                          [add_button, edit_button, complete_button, exit_buttton]],
                  font=("Helvetica", 16))

while True:
    event, values = window.read(timeout=500)
    window["clock"].update(value=time.strftime("%b %d, %Y %H:%M:%S"))
    # print(event)
    # print(values)

    match event:
        case "Add":
            todos = functions.get_todos()
            todos.append(values["todo"] + "\n")
            functions.write_todos(todos)
            window["todos"].update(values=todos)

        case "Edit":
            try:    
                to_edit_todo = values["todos"][0]

                todos = functions.get_todos()
                index = todos.index(to_edit_todo)
                
                todos[index] = values["todo"] + "\n"
                functions.write_todos(todos)
                window["todos"].update(values=todos)
            except IndexError:
                sg.popup("Please select an item first", font=("Helvetica", 16))

        case "todos":
            window["todo"].update(value=values["todos"][0])

        case "Complete":
            try:    
                to_remove_todo = values["todos"][0]
            
                todos = functions.get_todos()
                todos.remove(to_remove_todo)

                functions.write_todos(todos)
                
                window["todos"].update(values=todos)
                window["todo"].update(value="")
            except IndexError:
                sg.popup("Please select an item first", font=("Helvetica", 16))

        # Difference between break and exit()
        # exit() stops the program completely whereas the break statement only stops the loop
        case sg.WIN_CLOSED | "Exit":    
            break

window.close()
