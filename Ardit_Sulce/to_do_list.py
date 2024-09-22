# List comprehension in action

# filenames = ["filename-1", "filename-2", "filename-3"]
# filenames = [filename.replace("-",".") + ".txt" for filename in filenames]
# print(filenames)



# Zip function

# filenames = ["filename1.txt", "filename2.txt", "filename3.txt"]
# contents = ["content number one", "content number two", "content number three"]

# for filename, content in zip(filenames, contents):
#     file = open(f"../files/{filename}", "w")
#     file.write(content)




# Enumerate function

# waiting_list = ["sen", "ben", "john"]
# waiting_list.sort()

# for index, item in enumerate(waiting_list,start=1):
#     print(f"{index} -{item.capitalize()}")





# user_prompt = input("Enter a password: ")

# while user_prompt != "secret":
#     print("You entered incorrect password")
#     user_prompt = input("Enter a password: ")


# print("You entered the correct password")




# n = 6
# while n > 0:
#     print(n)
#     n -= 1

# print(dir("Hello"))
# help(str.capitalize)



# import builtins
# print(dir(builtins))



while True:
    user_action = input("Type add, show, edit, complete or exit: ")

    match user_action.strip():

        case "add":
            todo = input("Enter a todo: ") + "\n"

            # file = open("todos.txt", "r")
            # todos = file.readlines()
            # file.close()

            with open("todos.txt", "r") as file:
                todos = file.readlines()

            todos.append(todo)

            with open("todos.txt", "w") as file:
                file.writelines(todos)
            
        case "show" | "display":

            with open("todos.txt", "r") as file:
                todos = file.readlines()
            
            # new_todos = [item.strip("\n") for item in todos]

            for index, item in enumerate(todos, start = 1):
                print(f"{index} -{item.strip("\n")}")

        case "edit":
            with open("todos.txt", "r") as file:
                todos = file.readlines()
            
            to_change_index = int(input("Enter todo number: "))
            new_todo = input("Enter the changed todo: ") + "\n"
            todos[to_change_index - 1] = new_todo

            with open("todos.txt", "w") as file:
                file.writelines(todos)
            
        case "complete":
            with open("todos.txt", "r") as file:
                todos = file.readlines()
                        
            number = int(input("Enter number of the todo: "))
            removed_todo = todos[number - 1].strip("\n")
            todos.pop(number - 1)

            with open("todos.txt", "w") as file:
                file.writelines(todos) 

            print(f"Todo {removed_todo} was removed from the list")     

        case "exit":
            break

        case whatever:
            print("You entered unknown command")

print("Bye")

