


# Concept of DECOUPLING, wherein a function that performs multiple tasks is broken down into separate functions each performing a singular task, so that the output of those singular tasks can be accessed anywhere else in the program.

# In the below code, instead of using one function to perform both the tasks, two functions have been defined. One function parses the string which is received from the user and the second function converts to meters.

# Here, since the function has been decoupled into two, the local variables like feet and inches can be returned and can be used at other places in the program, which would have been impossible, had both the functions been defined in a single one.

# def parse(feet_inches):
#     parts = feet_inches.split(" ")
#     feet = float(parts[0])
#     inches = float(parts[1])
#     return dict(feet=feet, inches=inches)

# def convert(feet, inches):
#     return feet * 0.3048 + inches * 0.0254

# feet_inches = input("Enter feet and inches: ")

# parsed = parse(feet_inches)

# result = convert(parsed["feet"], parsed["inches"])

# print(f"{parsed['feet']} feet and {parsed['inches']} is equal to {result} ")

# if result < 1:
#     print("Kid is too small")
# else:
#     print("Kid is eligible to use the slide")











# def get_temp_avg(filename):
#     with open(filename, "r") as file_local:
#         data = file_local.readlines()
#     values = data[1:]
#     values = [float(item) for item in values]

#     average_local = sum(values)/len(values) 
#     return average_local


# average = get_temp_avg("data.txt")
# print(average)





# day_temperature = dict(morning = (22.3,21.2), evening = (10.2, 9.4))
# print(day_temperature["morning"])



# Check if the password is strong using concept of list and dictionary
# The keys of the dictionary are metadata 
# password = input("Enter a password: ")

# result = []
# result = {}

# if len(password) >= 8:
#     # result.append(True)
#     result["length"] = True
    
# else:
#     # result.append(False)
#     result["length"] = False

# digit = False
# for i in password:
#     if i.isdigit():
#         digit = True

# result["digit"] = digit

# upper = False
# for i in password:
#     if i.isupper():
#         upper = True

# result["upper"] = upper

# print(result)
# print(all(result.values()))
# if all(result.values()):
#     print("Strong password")
# else:
#     print("Weak password")







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


# TO DO LIST CODE WITH MATCH CASE 

# while True:
#     user_action = input("Type add, show, edit, complete or exit: ")

#     match user_action.strip():

#         case "add":
#             todo = input("Enter a todo: ") + "\n"

#             # file = open("todos.txt", "r")
#             # todos = file.readlines()
#             # file.close()

#             with open("todos.txt", "r") as file:
#                 todos = file.readlines()

#             todos.append(todo)

#             with open("todos.txt", "w") as file:
#                 file.writelines(todos)
            
#         case "show" | "display":

#             with open("todos.txt", "r") as file:
#                 todos = file.readlines()
            
#             # new_todos = [item.strip("\n") for item in todos]

#             for index, item in enumerate(todos, start = 1):
#                 print(f"{index} -{item.strip("\n")}")

#         case "edit":
#             with open("todos.txt", "r") as file:
#                 todos = file.readlines()
            
#             to_change_index = int(input("Enter todo number: "))
#             new_todo = input("Enter the changed todo: ") + "\n"
#             todos[to_change_index - 1] = new_todo

#             with open("todos.txt", "w") as file:
#                 file.writelines(todos)
            
#         case "complete":
#             with open("todos.txt", "r") as file:
#                 todos = file.readlines()
                        
#             number = int(input("Enter number of the todo: "))
#             removed_todo = todos[number - 1].strip("\n")
#             todos.pop(number - 1)

#             with open("todos.txt", "w") as file:
#                 file.writelines(todos) 

#             print(f"Todo {removed_todo} was removed from the list")     

#         case "exit":
#             break

#         case whatever:
#             print("You entered unknown command")

# print("Bye")

# TO DO LIST CODE WITH IF ELSE

# By using the function get_todos(), the following two lines of codes, which were used to read todos.txt are being replaced with todos = get_todos()

# with open("todos.txt", "r") as file:
    # todos = file.readlines()

# def get_todos(filepath="todos.txt"):
#     with open("todos.txt", "r") as file_local:
#         return file_local.readlines()
    
# Likewise, the following two lines are replaced by write_todos(todos)
# with open("todos.txt", "w") as file:
#                 file.writelines(todos)

# def write_todos(todos_local, filepath="todos.txt"):
#     with open("filepath", "w") as file:
#         file.writelines(todos_local)    

# from functions import get_todos, write_todos
import functions
import time

now = time.strftime("%b %d, %Y %H:%M:%S")
print("It is", now)

while True:
    user_action = input("Type add, show, edit, complete or exit: ")

    # if "add" in user_action:

        # todo = input("Enter a todo: ") + "\n"

        # file = open("todos.txt", "r")
        # todos = file.readlines()
        # file.close()
    if user_action.startswith("add"):

        todos = functions.get_todos()

        todos.append(user_action[4:] + "\n")
         
        functions.write_todos(todos)
            
    elif user_action.startswith("show"):

        todos = functions.get_todos()

        # new_todos = [item.strip("\n") for item in todos]

        for index, item in enumerate(todos, start = 1):
            print(f"{index} -{item.strip("\n")}")

    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:]) - 1
           
            todos = functions.get_todos()

            new_todo = input("Enter the changed todo: ") + "\n"
            todos[number] = new_todo

            functions.write_todos(todos)

        except ValueError:
            print("Invalid command.")
            
            

    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:]) - 1
                      
            todos = functions.get_todos()
                        
            removed_todo = todos[number].strip("\n")
            todos.pop(number) 

            functions.write_todos(todos)

            print(f"Todo {removed_todo} was removed from the list")  

        except ValueError:
            print("Invalid command")
        except IndexError:
            print("There is no item with that number")

    elif user_action.startswith("exit"):
        break

    else:
        print("You entered unknown command")

print("Bye")

