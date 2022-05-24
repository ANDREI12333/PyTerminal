import os

def clear():
    os.system("cls")

while True:
    user = os.getlogin()
    userinput = input(user+": ")
    if userinput == "exit":
        clear()
        print("Bye!")
        quit()
    elif userinput == "clear":
        clear()
    else:
        print("Unknown command.")
