from colorama import Fore
import os
import platform
import random
import string


todo_list = []


print(Fore.LIGHTYELLOW_EX+"""
    ########################
           import life
    ########################  
    """+Fore.RESET)

while True:
    question = input(Fore.GREEN+"\n~"+Fore.RESET).lower()

    if question == "cls" or question == "clear":
        os.system("cls" or "clear")
        print(Fore.LIGHTYELLOW_EX+"""
    ########################
          import life
    ########################  
    """+Fore.RESET)

    elif question == "exit":
        exit()

    elif question == "python":
        os.system("python")
        
    elif question[0:6] == "python":
        os.system(f"python {question[6:]}")
    
    elif question == "explorer":
        os.system("explorer")
        print("explorer opened...")
    
    elif question[0:5] == "color":
        os.system(f"color {question[5:]}")
        
    elif question[0:4] == "more":
        os.system(f"more {question[4:]}")

    elif question == "sys_version":
        print(platform.system(), platform.version())

    elif question == "sys_information":
        for s_i in platform.uname():
            print(s_i)

    elif question == "install_pack":
        pack_name = input("@pack-name@ ")
        if pack_name:
            os.system(f"pip install {pack_name}")            
    elif question == "run":
        os.system("start powershell")

    elif question[0:3] == "run":
        os.system(f"start {question[3:]}")
    
    elif question == "create_fold":
        fold_rand_name = random.choice(string.ascii_letters)
        os.system(f"mkdir {fold_rand_name}")
        print(f"folder {fold_rand_name} created...")
        
    elif question[0:len("create_fold")] == "create_fold":
        os.system(f"mkdir {question[11:]}")
        print("folder {fold_name}".format(fold_name=question[11:]))
        
    elif question == "todo list":
        while True:
            try:
                get_day = int(input("Enter todo day:"))
                get_todo = input("Enter todo text:").lower()
                if get_todo and get_todo != "end":
                    todo_list.append([get_day, get_todo])
                else:
                    if get_todo == False:
                        print("Error.")
                    else:
                        break
            except ValueError:
                print("Canceled")
                break
            
    elif question == "show todo list":
        if todo_list:
            for lists in todo_list:
                print(f"day [{lists[0]}] todo text is [{lists[1][0:5]}...]")
        else:
            print("list is empty!")
    
#     elif question == "delete todo text": # this part has error and bug...
#         if todo_list:
#             for lists in todo_list:
#                 print(f"day [{lists[0]}] todo test is : [{lists[1]}]")
#             while True:
#                 try:
#                     get_deleting_day = int(input("Enter todo day to delete them...:"))
#                     for lists in todo_list:
#                         pass
#                     if get_deleting_day == lists[0]:
#                         lists.pop()
#                         print(f"deleted {lists[1]}")
#                     else:
#                         print(f"not found day{get_deleting_day}")
#                 except ValueError:
#                     print(get_deleting_day)
              
    else:
        print(Fore.LIGHTRED_EX+f"command \"{question}\" not found..."+Fore.RESET)
