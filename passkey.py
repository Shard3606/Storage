UL = 0

def signup():
    name = input("Please make a username: ")

    print ("Your username has been created and is", name, ".")

    password = input("Now please create a password: ")

    file = open("Login.txt","a")
    file.write (name)
    file.write (",")
    file.write (password)
    file.write("\n")
    file.close()

    print ("Your login details have been saved. ")

def login(file_path):
    global UL
    name = input("Enter your username: ")
    password = input("Enter your password: ")
    user = name + "," + password
    with open(file_path, 'r') as file:
        # read all content of a file
        content = file.read()
        # check if string present in a file
        if user in content:
            print("Logged in")
            UL = 1
        else:
            print("Please create an account")

while UL == 0:
    LS = input("Would you like to (L)ogin or (S)ign Up?: ")
    if LS == "l" or LS == "L":
            login("Login.txt")
            if UL == 1:
                break
    elif LS == "s" or LS == "S":
            signup()
    else:
            print("Enter valid option")

print("Welcome to St0rage")
import mainmenu.py
