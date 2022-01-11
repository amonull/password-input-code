import main
from main import *
import os 
import importlib

try:#this line of code will allow for the program to encrypt the code so that the code can be properly used. and it will make sure that it doesnt end without encrypting first since it is in a while loop.
    while True:

        operation = input("choose operation:\nV = view file\nS = search for data\nA = append data\nD = delete data\nE = edit data\nQ = quit program and encrypt file.\n: ").lower()

        if operation == "v":
            app.view_file()

        elif operation == "s":
            app.search(input("\nenter the column you wish to search for: ").upper(), input("enter the value you wish to search for: "))

        elif operation == "a":
            print("\nif you have no data to enter in leave blank(press enter)")
            app.append(SITE=input("Enter the site name: "), USERNAME=input("Enter the username: "), PASSWORDS=input("Enter the password: "))

        elif operation == "d":#ERRORS this code usualy gives FUTURE_WARNING but it has been supressed check main.py for more info
            app.view_file()
            del_list = list(input("Choose the index number of item you wish to delete: "))
            if ' ' in del_list:
                del_list.remove(' ')
            del_items = [int(i) for i in del_list]# there may not be a need for this for loop as *args is used on main.py
            app.delete(del_items)

        elif operation == "e":
            app.view_file()
            app.edit(input("Enter the INDEX number of item you wish to edit: "), input("Enter the COLUMN you wish to edit from: ").upper(), input("Enter what you wish to change it to: "))


        elif operation == "q":
            app.shut_down()

        if input("press enter to continue: ") == "": #clears terminal after each loop so terminal doesnt get too crowded and reloads module so everything works live time without need of manual reloading.
            os.system('cls' if os.name == 'nt' else 'clear')
            importlib.reload(main)
            from main import *

except KeyboardInterrupt:
    app.shut_down()
