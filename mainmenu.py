import time
import re
import os
UL = 0

Lists = []
Selection = ""
List1 = ("ListName")
List1Number = ["ListNumber"]
List1Items = ["ListItems"]
List2 = ("ListName")
List2Number = ["ListNumber"]
List2Items = ["ListItems"]
List3 = ("ListName")
List3Number = ["ListNumber"]
List3Items = ["ListItems"]
List4 = ("ListName")
List4Number = ["ListNumber"]
List4Items = ["ListItems"]
List5 = ("ListName")
List5Number = ["ListNumber"]
List5Items = ["ListItems"]

def clear():
    screen_clear = 'Clearing Screen .'
    print(screen_clear)
    time.sleep(.3)
    print(screen_clear + ' .')
    time.sleep(.3)
    print(screen_clear + ' . .')
    time.sleep(.3)
    os.system('cls')

def CreateList():
    global List1
    global List2
    global List3
    global List4
    global List5
    global List1Number
    global List2Number
    global List3Number
    global List4Number
    global List5Number
    global List1Items
    global List2Items
    global List3Items
    global List4Items
    global List5Items
    global name
    clear()
    ListText = []
    ListNumber = []
    TempListName = input("What would you like the name of the List to be? Or input 'Back' to go back.")
    if TempListName.lower() == str("back"):
        Welcome()
    elif TempListName == ("ListName"):
        print ("Please select a different list name.")
        time.sleep(3)
        CreateList ()
    print(str(TempListName))
    print('\n')
    while True:
        ListText.append(input("What object would you like to add? (Type 'Quit' (Must be with a capital Q) when you are done.)"))
        if ListText.count("Quit") > 0:
            ListText.remove("Quit")
            break
        ListNumber.append(input("How many of this object do you currently have?"))
    if List1 == ("ListName"):
        List1 = str(TempListName)
        List1Items = ListText
        List1Number = ListNumber
        print("Saving List...")
    elif List2 == ("ListName"):
        List2 = str(TempListName)
        List2Items = ListText
        List2Number = ListNumber
        print("Saving List...")
    elif List3 == ("ListName"):
        List3 = str(TempListName)
        List3Items = ListText
        List3Number = ListNumber
        print("Saving List...")
    elif List4 == ("ListName"):
        List4 = str(TempListName)
        List4Items = ListText
        List4Number = ListNumber
        print("Saving List...")
    elif List5 == ("ListName"):
        List5 = str(TempListName)
        List5Items = ListText
        List5Number = ListNumber
        print("Saving List...")
    else:
        print("Out of space, please delete a List to continue.")
    time.sleep(3)
    Welcome()

def EditList():
    global List1
    global List2
    global List3
    global List4
    global List5
    global List1Number
    global List2Number
    global List3Number
    global List4Number
    global List5Number
    global List1Items
    global List2Items
    global List3Items
    global List4Items
    global List5Items
    if List1 != ("ListName"):
        print(List1)
        print(List1Items)
        print(List1Number)
    if List2 != ("ListName"):
        print(List2)
        print(List2Items)
        print(List2Number)
    if List3 != ("ListName"):
        print(List3)
        print(List3Items)
        print(List3Number)
    if List4 != ("ListName"):
        print(List4)
        print(List4Items)
        print(List4Number)
    if List5 != ("ListName"):
        print(List5)
        print(List5Items)
        print(List5Number)
    ListSelection = input("Please input the name of the List you would like to edit, or input 'Back' to go back.")
    if ListSelection.lower() == List1.lower():
        print(List1)
        print(List1Items)
        print(List1Number)
        TextorNumber = input("Would you like to edit the (I)tems on your list or the (N)umber?")
        if TextorNumber.lower() == "i":
            choiceselection = input("Would you like to (A)dd something on the list, (E)dit something on the list, or (R)emove something from the list?")
            if choiceselection.lower() == "a":
                while True:
                    List1Items.append(input("What object would you like to add? (Type 'Quit' (Must be with a capital Q) when you are done.)"))
                    if List1Items.count("Quit") > 0:
                        List1Items.remove("Quit")
                        break
                    List1Number.append(input("How many of this object do you currently have?"))
            if choiceselection.lower() == "e":
                itemchoice = int(input("Which item would you like to edit? (Use the number correspondent to the item)"))
                List1Items[itemchoice - 1] = input("What new item would you like?")
            if choiceselection.lower() == "r":
                itemchoice = int(input("Which item would you like to remove? (Use the number correspondent to the item)"))
                List1Items.pop(itemchoice - 1)
                List1Number.pop(itemchoice - 1)
        if TextorNumber.lower() == "n":
            itemchoice = int(input("Which number would you like to edit? (Use the number correspondent to the item)"))
            List1Number[itemchoice - 1] = input("What new number would you like?")
        EditList()
    if ListSelection.lower() == List2.lower():
        print(List2)
        print(List2Items)
        print(List2Number)
        TextorNumber = input("Would you like to edit the (I)tems on your list or the (N)umber?")
        if TextorNumber.lower() == "i":
            choiceselection = input("Would you like to (A)dd something on the list, (E)dit something on the list, or (R)emove something from the list?")
            if choiceselection.lower() == "a":
                while True:
                    List2Items.append(input("What object would you like to add? (Type 'Quit' (Must be with a capital Q) when you are done.)"))
                    if List2Items.count("Quit") > 0:
                        List2Items.remove("Quit")
                        break
                    List2Number.append(input("How many of this object do you currently have?"))
            if choiceselection.lower() == "e":
                itemchoice = int(input("Which item would you like to edit? (Use the number correspondent to the item)"))
                List2Items[itemchoice - 1] = input("What new item would you like?")
            if choiceselection.lower() == "r":
                itemchoice = int(input("Which item would you like to remove? (Use the number correspondent to the item)"))
                List2Items.pop(itemchoice - 1)
                List2Number.pop(itemchoice - 1)
        if TextorNumber.lower() == "n":
            itemchoice = int(input("Which number would you like to edit? (Use the number correspondent to the item)"))
            List2Number[itemchoice - 1] = input("What new number would you like?")
        EditList()
    if ListSelection.lower() == List3.lower():
        print(List3)
        print(List3Items)
        print(List3Number)
        TextorNumber = input("Would you like to edit the (I)tems on your list or the (N)umber?")
        if TextorNumber.lower() == "i":
            choiceselection = input("Would you like to (A)dd something on the list, (E)dit something on the list, or (R)emove something from the list?")
            if choiceselection.lower() == "a":
                while True:
                    List3Items.append(input("What object would you like to add? (Type 'Quit' (Must be with a capital Q) when you are done.)"))
                    if List3Items.count("Quit") > 0:
                        List3Items.remove("Quit")
                        break
                    List3Number.append(input("How many of this object do you currently have?"))
            if choiceselection.lower() == "e":
                itemchoice = int(input("Which item would you like to edit? (Use the number correspondent to the item)"))
                List3Items[itemchoice - 1] = input("What new item would you like?")
            if choiceselection.lower() == "r":
                itemchoice = int(input("Which item would you like to remove? (Use the number correspondent to the item)"))
                List3Items.pop(itemchoice - 1)
                List3Number.pop(itemchoice - 1)
        if TextorNumber.lower() == "n":
            itemchoice = int(input("Which number would you like to edit? (Use the number correspondent to the item)"))
            List3Number[itemchoice - 1] = input("What new number would you like?")
        EditList()
    if ListSelection.lower() == List4.lower():
        print(List4)
        print(List4Items)
        print(List4Number)
        TextorNumber = input("Would you like to edit the (I)tems on your list or the (N)umber?")
        if TextorNumber.lower() == "i":
            choiceselection = input("Would you like to (A)dd something on the list, (E)dit something on the list, or (R)emove something from the list?")
            if choiceselection.lower() == "a":
                while True:
                    List4Items.append(input("What object would you like to add? (Type 'Quit' (Must be with a capital Q) when you are done.)"))
                    if List4Items.count("Quit") > 0:
                        List4Items.remove("Quit")
                        break
                    List4Number.append(input("How many of this object do you currently have?"))
            if choiceselection.lower() == "e":
                itemchoice = int(input("Which item would you like to edit? (Use the number correspondent to the item)"))
                List4Items[itemchoice - 1] = input("What new item would you like?")
            if choiceselection.lower() == "r":
                itemchoice = int(input("Which item would you like to remove? (Use the number correspondent to the item)"))
                List4Items.pop(itemchoice - 1)
                List4Number.pop(itemchoice - 1)
        if TextorNumber.lower() == "n":
            itemchoice = int(input("Which number would you like to edit? (Use the number correspondent to the item)"))
            List4Number[itemchoice - 1] = input("What new number would you like?")
        EditList()
    if ListSelection.lower() == List5.lower():
        print(List5)
        print(List5Items)
        print(List5Number)
        TextorNumber = input("Would you like to edit the (I)tems on your list or the (N)umber?")
        if TextorNumber.lower() == "i":
            choiceselection = input("Would you like to (A)dd something on the list, (E)dit something on the list, or (R)emove something from the list?")
            if choiceselection.lower() == "a":
                while True:
                    List5Items.append(input("What object would you like to add? (Type 'Quit' (Must be with a capital Q) when you are done.)"))
                    if List5Items.count("Quit") > 0:
                        List5Items.remove("Quit")
                        break
                    List5Number.append(input("How many of this object do you currently have?"))
            if choiceselection.lower() == "e":
                itemchoice = int(input("Which item would you like to edit? (Use the number correspondent to the item)"))
                List5Items[itemchoice - 1] = input("What new item would you like?")
            if choiceselection.lower() == "r":
                itemchoice = int(input("Which item would you like to remove? (Use the number correspondent to the item)"))
                List5Items.pop(itemchoice - 1)
                List5Number.pop(itemchoice - 1)
        if TextorNumber.lower() == "n":
            itemchoice = int(input("Which number would you like to edit? (Use the number correspondent to the item)"))
            List5Number[itemchoice - 1] = input("What new number would you like?")
        EditList()
    if ListSelection.lower() == "back":
        Welcome()
    else:
        print("Please make sure to write one of the valid List names.")
        time.sleep(3)
        EditList()


def ViewList():
    global List1
    global List2
    global List3
    global List4
    global List5
    clear()
    lstuser = input("Enter your username: ")
    lstpass = input("Enter your password: ")
    lstfile_path = str(lstuser.lower()) + "," + str(lstpass.lower())

    try:
        with open(lstfile_path, 'r') as file:
            # Read the content of the file
            file_content = file.read()

            # Print the content
            print("File Content:\n", file_content)

    except FileNotFoundError:
        print(f"File '{lstfile_path}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
    back = input("Type anything when you're done: ")
    if back == "anything":
        print("Funny guy")
        time.sleep(2)
        Welcome()
    elif back == "SECRET CODE":
        print("▄▀▄▀▀▀▀▄▀▄░░░░░░░░░░" + "\n" + "█░░░░░░░░▀▄░░░░░░▄░░" + "\n" + "█░░▀░░▀░░░░░▀▄▄░░█░█" + "\n" + "█░▄░█▀░▄░░░░░░░▀▀░░█" + "\n" +"█░░▀▀▀▀░░░░░░░░░░░░█"+ "\n" +"█░░░░░░░░░░░░░░░░░░█"+ "\n" +"░█░░▄▄░░▄▄▄▄░░▄▄░░█░"+ "\n" +"░█░▄▀█░▄▀░░█░▄▀█░▄▀░"+ "\n" +"░░▀░░░▀░░░░░▀░░░▀░░░")
    else:
        Welcome()


def DeleteList():
    global List1
    global List2
    global List3
    global List4
    global List5
    global List1Number
    global List2Number
    global List3Number
    global List4Number
    global List5Number
    global List1Items
    global List2Items
    global List3Items
    global List4Items
    global List5Items
    clear()
    if List1 != ("ListName"):
        print(List1)
    if List2 != ("ListName"):
        print(List2)
    if List3 != ("ListName"):
        print(List3)
    if List4 != ("ListName"):
        print(List4)
    if List5 != ("ListName"):
        print(List5)
    ListSelection = input("Please input the name of the List you would like to delete, or input 'Back' to go back.")
    if ListSelection == List1:
        print(List1)
        Sure = input("Are you sure you want to delete this List? Input N for no and Y for yes.")
        if Sure == "Y":
            List1 = ("ListName")
            List1Number = ["ListNumber"]
            print("Deleting List...")
        elif Sure == "N":
            Continue = ""
    elif ListSelection == List2:
        print(List2)
        Sure = input("Are you sure you want to delete this List? Input N for no and Y for yes.")
        if Sure == "Y":
            List2 = ("ListName")
            List2Number = ["ListNumber"]
            print("Deleting List...")
        elif Sure == "N":
            Continue = ""
    elif ListSelection == List3:
        print(List3)
        Sure = input("Are you sure you want to delete this List? Input N for no and Y for yes.")
        if Sure == "Y":
            List3 = ("ListName")
            List3Number = ["ListNumber"]
            print("Deleting List...")
        elif Sure == "N":
            Continue = ""
    elif ListSelection == List4:
        print(List4)
        Sure = input("Are you sure you want to delete this List? Input N for no and Y for yes.")
        if Sure == "Y":
            List4 = ("ListName")
            List4Number = ["ListNumber"]
            print("Deleting List...")
        elif Sure == "N":
            Continue = ""
    elif ListSelection == List5:
        print(List5)
        Sure = input("Are you sure you want to delete this List? Input N for no and Y for yes.")
        if Sure == "Y":
            List5 = ("ListName")
            List5Number = ["ListNumber"]
            print("Deleting List...")
        elif Sure == "N":
            Continue = ""
    elif ListSelection.lower() == "back":
        Continue = ""
    else:
        print("Please make sure to write one of the valid List names.")
        time.sleep(3)
        DeleteList()
    #Fetch List list and List, print List
    time.sleep(3)
    Welcome()

def Logout():
    print("Come back soon!")
    clear()
    global UL
    UL = 0
    time.sleep(3)
    Welcome()

def signup():
    name = input("Please make a username: ")

    print ("Your username has been created and is ", name, ".")

    password = input("Now please create a password: ")

    lgnfile = open("Login.txt","a")
    lgnfile.write (name)
    lgnfile.write (",")
    lgnfile.write (password)
    lgnfile.write("\n")
    lgnfile.close()
    list1file = open("List1" + name + ".txt","w")
    list1file.writelines (List1)
    list1file.write ("\n")
    list1file.writelines (str(List1Items))
    list1file.write ("\n")
    list1file.writelines (str(List1Number))
    list1file.close()
    list2file = open("List2" + name + ".txt","w")
    list2file.writelines (List2)
    list2file.write ("\n")
    list2file.writelines (str(List2Items))
    list2file.write ("\n")
    list2file.writelines (str(List2Number))
    list2file.close()
    list3file = open("List3" + name + ".txt","w")
    list3file.writelines (List3)
    list3file.write ("\n")
    list3file.writelines (str(List3Items))
    list3file.write ("\n")
    list3file.writelines (str(List3Number))
    list3file.close()
    list4file = open("List4" + name + ".txt","w")
    list4file.writelines (List4)
    list4file.write ("\n")
    list4file.writelines (str(List4Items))
    list4file.write ("\n")
    list4file.writelines (str(List4Number))
    list4file.close()
    list5file = open("List5" + name + ".txt","w")
    list5file.writelines (List5)
    list5file.write ("\n")
    list5file.writelines (str(List5Items))
    list5file.write ("\n")
    list5file.writelines (str(List5Number))
    list5file.close()

    print ("Your login details have been saved. ")

def login(lgnfile_path):
    global List1
    global List2
    global List3
    global List4
    global List5
    global List1Number
    global List2Number
    global List3Number
    global List4Number
    global List5Number
    global List1Items
    global List2Items
    global List3Items
    global List4Items
    global List5Items
    global UL
    global name
    name = input("Enter your username: ")
    password = input("Enter your password: ")
    user = name + "," + password
    login_successful = False

    with open(lgnfile_path, 'r') as file:
        for line_number, line in enumerate(file, start=1):
            if re.search(r'\b{}\b'.format(re.escape(user)), line):
                login_successful = True
                break  # Exit the loop once login is successful

    if login_successful:
        print("Logged in")
        UL = 1
    else:
        print("Please create an account")
    list1file = open("List1" + name + ".txt","r")
    list1clear = list1file.readline()
    if list1clear[0] != ("ListName"):
        List1 = list1clear[0]
        List1Number = list1clear[1]
        List1Items = list1clear[2]
    else:
        List1 = ("ListName")
        List1Number = ["ListNumber"]
        List1Items = ["ListItems"]
    list1file.close
    list2file = open("List2" + name + ".txt","r")
    list2clear = list2file.readline()
    if list2clear[0] != ("ListName"):
        List2 = list2clear[0]
        List2Number = list2clear[1]
        List2Items = list2clear[2]
    else:
        List2 = ("ListName")
        List2Number = ["ListNumber"]
        List2Items = ["ListItems"]
    list2file.close
    list3file = open("List3" + name + ".txt","r")
    list3clear = list3file.readline()
    if list3clear[0] != ("ListName"):
        List3 = list3clear[0]
        List3Number = list3clear[1]
        List3Items = list3clear[2]
    else:
        List3 = ("ListName")
        List3Number = ["ListNumber"]
        List3Items = ["ListItems"]
    list3file.close
    list4file = open("List4" + name + ".txt","r")
    list4clear = list4file.readline()
    if list4clear[0] != ("ListName"):
        List4 = list4clear[0]
        List4Number = list4clear[1]
        List4Items = list4clear[2]
    else:
        List4 = ("ListName")
        List4Number = ["ListNumber"]
        List4Items = ["ListItems"]
    list4file.close
    list5file = open("List5" + name + ".txt","r")
    list5clear = list5file.readline()
    if list5clear[0] != ("ListName"):
        List5 = list5clear[0]
        List5Number = list5clear[1]
        List5Items = list5clear[2]
    else:
        List5 = ("ListName")
        List5Number = ["ListNumber"]
        List5Items = ["ListItems"]
    list5file.close

def Welcome():
    global Selection
    global UL
    global List1
    global List2
    global List3
    global List4
    global List5
    global List1Number
    global List2Number
    global List3Number
    global List4Number
    global List5Number
    global List1Items
    global List2Items
    global List3Items
    global List4Items
    global List5Items

    clear()

    while UL == 0:
        LS = input("Would you like to (L)ogin or (S)ign Up?: ")
        if LS == "l" or LS == "L":
                login("Login.txt")
        elif LS == "s" or LS == "S":
                signup()
        else:
                print("Enter valid option")


    print("Welcome to St0rage")

    Selection = input("Write 'C' if you would like to create a List," '\n'
                  "write 'E' if you would like to edit an existing List," '\n'
                  "write 'V' if you would like to view an existing List," '\n'
                  "write 'D' if you would like to delete an existing List," '\n'
                  "write 'S' if you would like to save your progress so far," '\n'
                  "write 'DA' if you want to delete your account," '\n'
                  "or write 'L' if you would like to log out: ")
    if Selection.lower() == "c":
        CreateList()
    elif Selection.lower() == "e":
        EditList()
    elif Selection.lower() == "v":
        ViewList()
    elif Selection.lower() == "d":
        DeleteList()
        DeleteList()
    elif Selection.lower() == "s":
        list1file = open("List1" + name + ".txt","w")
        list1file.writelines (List1)
        list1file.write ("\n")
        list1file.writelines (str(List1Items))
        list1file.write ("\n")
        list1file.writelines (str(List1Number))
        list1file.close()
        list2file = open("List2" + name + ".txt","w")
        list2file.writelines (List2)
        list2file.write ("\n")
        list2file.writelines (str(List2Items))
        list2file.write ("\n")
        list2file.writelines (str(List2Number))
        list2file.close()
        list3file = open("List3" + name + ".txt","w")
        list3file.writelines (List3)
        list3file.write ("\n")
        list3file.writelines (str(List3Items))
        list3file.write ("\n")
        list3file.writelines (str(List3Number))
        list3file.close()
        list4file = open("List4" + name + ".txt","w")
        list4file.writelines (List4)
        list4file.write ("\n")
        list4file.writelines (str(List4Items))
        list4file.write ("\n")
        list4file.writelines (str(List4Number))
        list4file.close()
        list5file = open("List5" + name + ".txt","w")
        list5file.writelines (List5)
        list5file.write ("\n")
        list5file.writelines (str(List5Items))
        list5file.write ("\n")
        list5file.writelines (str(List5Number))
        list5file.close()
        print ("Saving...")
        time.sleep(3)
        Welcome()
    elif Selection.lower() == "l":
        Logout()
    elif Selection.lower() == "da":
        DeleteAccount(lgnfile = open("Login.txt","a"))
    else:
        "Please make sure to input one of the available options."
        time.sleep(3)
        Welcome()

def DeleteAccount(lgnfile = open("Login.txt","a")):
    global UL
    global name
    global password
    global user
    clear()
    usure = input("Are you sure you would like to delete your account (Y/N)")
    if usure.lower() == "y":
        with open('login.txt', 'r') as fr:
            user = fr.readlines()

            with open('Login.txt', 'w') as fw:
                for line in user:

                    # find() returns -1
                    # if no match found
                    if line.find('user') == -1:
                        fw.write(line)
                        UL = 0
                        Welcome()
    if usure.lower() == "n":
        Welcome()
    else:
        print("Please enter a valid option")
        DeleteAccount()


Welcome()
