import time
UL = 0

Lists = []
Selection = ""
List1 = ("")
List1Number = ["ListNumber"]
List1Items = ["ListItems"]
List2 = ("")
List2Number = ["ListNumber"]
List2Items = ["ListItems"]
List3 = ("")
List3Number = ["ListName"]
List3Items = ["ListItems"]
List4 = ("")
List4Number = ["ListName"]
List4Items = ["ListItems"]
List5 = ("")
List5Number = ["ListName"]
List5Items = ["ListItems"]

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
    ListText = []
    ListNumber = []
    TempListName = input("What would you like the name of the List to be? Or input 'Back' to go back.")
    if TempListName == str("Back"):
        Welcome()
    elif TempListName == ("ListName"):
        print ("Please select a different list name.")
        time.sleep(3)
        CreateList ()
    print(str(TempListName))
    print('\n')
    while True:
        ListText.append(input("What object would you like to add? (Type 'Quit' when you are done.)"))
        if ListText.count("Quit") > 0:
            ListText.remove("Quit")
            break
        ListNumber.append(input("How many of this object do you currently have?"))
    if List1 == (""):
        List1 = str(TempListName)
        List1Items = ListText
        List1Number = ListNumber
        print("Saving List...")
    elif List2 == (""):
        List2 = str(TempListName)
        List2Number = ListText
        print("Saving List...")
    elif List3 == (""):
        List3 = str(TempListName)
        List3Number = ListText
        print("Saving List...")
    elif List4 == (""):
        List4 = str(TempListName)
        List4Number = ListText
        print("Saving List...")
    elif List5 == (""):
        List5 = str(TempListName)
        List5Number = ListText
        print("Saving List...")
    else:
        print("Out of space, please delete a List to continue.")
    #Save List Text to Database
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
    if List1 != (""):
        print(List1)
        print(List1Items)
        print(List1Number)
    if List2 != (""):
        print(List2)
        print(List2Items)
        print(List2Number)
    if List3 != (""):
        print(List3)
        print(List3Items)
        print(List3Number)
    if List4 != (""):
        print(List4)
        print(List4Items)
        print(List4Number)
    if List5 != (""):
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
                itemchoice = int(input("Which item would you like to edit? (Use the number correspondent to the item)")) - 1
                List1Items[itemchoice] = input("What new item would you like?")
            if choiceselection.lower() == "r":
            
                itemchoice = int(input("Which item would you like to remove? (Use the number correspondent to the item)")) - 1
                List1Items.remove(itemchoice)
                List1Number.remove(itemchoice)
        if TextorNumber.lower() == "n":
            itemchoice = int(input("Which number would you like to edit? (Use the number correspondent to the item)")) - 1
            List1Number[itemchoice] = input("What new number would you like?")
    elif ListSelection.lower() == List2.lower():
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
                itemchoice = input("Which item would you like to edit? (Use the number correspondent to the item)")
                List2Items[itemchoice] = input("What new item would you like?")
            if choiceselection.lower() == "r":
                itemchoice = input("Which item would you like to remove? (Use the number correspondent to the item)")
                List2Items.remove(itemchoice)
                List2Number.remove(itemchoice)
        if TextorNumber.lower() == "n":
            itemchoice = input("Which number would you like to edit? (Use the number correspondent to the item)")
            List2Number[itemchoice] = input("What new number would you like?")
    elif ListSelection.lower() == List3.lower():
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
                itemchoice = input("Which item would you like to edit? (Use the number correspondent to the item)")
                List3Items[itemchoice] = input("What new item would you like?")
            if choiceselection.lower() == "r":
                itemchoice = input("Which item would you like to remove? (Use the number correspondent to the item)")
                List3Items.remove(itemchoice)
                List3Number.remove(itemchoice)
        if TextorNumber.lower() == "n":
            itemchoice = input("Which number would you like to edit? (Use the number correspondent to the item)")
            List3Number[itemchoice] = input("What new number would you like?")
    elif ListSelection.lower() == List4.lower():
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
                itemchoice = input("Which item would you like to edit? (Use the number correspondent to the item)")
                List4Items[itemchoice] = input("What new item would you like?")
            if choiceselection.lower() == "r":
                itemchoice = input("Which item would you like to remove? (Use the number correspondent to the item)")
                List4Items.remove(itemchoice)
                List4Number.remove(itemchoice)
        if TextorNumber.lower() == "n":
            itemchoice = input("Which number would you like to edit? (Use the number correspondent to the item)")
            List4Number[itemchoice] = input("What new number would you like?")
    elif ListSelection.lower() == List5.lower():
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
                itemchoice = input("Which item would you like to edit? (Use the number correspondent to the item)")
                List5Items[itemchoice] = input("What new item would you like?")
            if choiceselection.lower() == "r":
                itemchoice = input("Which item would you like to remove? (Use the number correspondent to the item)")
                List5Items.remove(itemchoice)
                List5Number.remove(itemchoice)
        if TextorNumber.lower() == "n":
            itemchoice = input("Which number would you like to edit? (Use the number correspondent to the item)")
            List5Number[itemchoice] = input("What new number would you like?")
    elif ListSelection.lower() == "back":
        Welcome()
    else:
        print("Please make sure to write one of the valid List names.")
        time.sleep(3)
        EditList()
    #Fetch List list and List, print List, make editable
    time.sleep(3)
    Welcome()

def ViewList():
    global List1
    global List2
    global List3
    global List4
    global List5
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


"""
def DeleteList():
    global List1
    global List2
    global List3
    global List4
    global List5
    List1[1] = List1Name
    List2[1] = List2Name
    List3[1] = List3Name
    List4[1] = List4Name
    List5[1] = List5Name
    if List1 != (""):
        print(List1[1])
    if List2 != (""):
        print(List2[1])
    if List3 != (""):
        print(List3[1])
    if List4 != (""):
        print(List4[1])
    if List5 != (""):
        print(List5[1])
    ListSelection = input("Please input the name of the List you would like to delete, or input 'Back' to go back.")
    if ListSelection == List1Name:
        print(List1[2])
        Sure = input("Are you sure you want to delete this List? Input N for no and Y for yes.")
        if Sure == "Y":
            List1 = ("")
            print("Deleting List...")
        elif Sure == "N":
            Continue = ""
    elif ListSelection == List2Name:
        print(List2[2])
        Sure = input("Are you sure you want to delete this List? Input N for no and Y for yes.")
        if Sure == "Y":
            List2 = ("")
            print("Deleting List...")
        elif Sure == "N":
            Continue = ""
    elif ListSelection == List3Name:
        print(List3[2])
        Sure = input("Are you sure you want to delete this List? Input N for no and Y for yes.")
        if Sure == "Y":
            List3 = ("")
            print("Deleting List...")
        elif Sure == "N":
            Continue = ""
    elif ListSelection == List4Name:
        print(List4[2])
        Sure = input("Are you sure you want to delete this List? Input N for no and Y for yes.")
        if Sure == "Y":
            List4 = ("")
            print("Deleting List...")
        elif Sure == "N":
            Continue = ""
    elif ListSelection == List5Name:
        print(List5[2])
        Sure = input("Are you sure you want to delete this List? Input N for no and Y for yes.")
        if Sure == "Y":
            List5 = ("")
            print("Deleting List...")
        elif Sure == "N":
            Continue = ""
    elif ListSelection == "Back":
        Continue = ""
    else:
        print("Please make sure to write one of the valid List names.")
        time.sleep(3)
        ViewList()
    #Fetch List list and List, print List
    time.sleep(3)
    Welcome()
    time.sleep(3)
    Welcome()
"""

def Logout():
    print("Come back soon!")
    time.sleep(3)

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

    print ("Your login details have been saved. ")
    
def login(lgnfile_path):
    global UL
    name = input("Enter your username: ")
    password = input("Enter your password: ")
    user = name + "," + password
    with open(lgnfile_path, 'r') as lgnfile:
        # read all content of a file
        content = lgnfile.read()
        # check if string present in a file
        if user in content:
            print("Logged in")
            UL = 1
        else:
            print("Please create an account")
        
def Welcome():
    global Selection
    global UL

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
                  "or write 'L' if you would like to log out: ")
    if Selection.lower() == "c":
        CreateList()
    elif Selection.lower() == "e":
        EditList()
    elif Selection.lower() == "v":
        ViewList()
    elif Selection.lower() == "d":
       print("DeleteList()")
    elif Selection.lower() == "l":
        Logout()
    else:
        "Please make sure to input one of the available options."
        time.sleep(3)
        Welcome()

Welcome()
