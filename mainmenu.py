import time
Lists = []
Selection = ""
List1 = ("")
List1Items = ["ListItems"]
List1Number = ["ListNumber"]
List2 = ("")
List2Items = ["ListItems"]
List2Number = ["ListNumber"]
List3 = ("")
List3Items = ["ListItems"]
List3Number = ["ListNumber"]
List4 = ("")
List4Items = ["ListItems"]
List4Number = ["ListNumber"]
List5 = ("")
List5Items = ["ListItems"]
List5Number = ["ListNumber"]

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
        List2Items = ListText
        List2Number = ListNumber
        print("Saving List...")
    elif List3 == (""):
        List3 = str(TempListName)
        List3Items = ListText
        List3Number = ListNumber
        print("Saving List...")
    elif List4 == (""):
        List4 = str(TempListName)
        List4Items = ListText
        List4Number = ListNumber
        print("Saving List...")
    elif List5 == (""):
        List5 = str(TempListName)
        List5Items = ListText
        List5Number = ListNumber
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
    if List2 != (""):
        print(List2)
    if List3 != (""):
        print(List3)
    if List4 != (""):
        print(List4)
    if List5 != (""):
        print(List5)
    ListSelection = input("Please input the name of the List you would like to edit, or input 'Back' to go back.")
    if ListSelection == List1:
        print(List1)
        print(List1Number)
        TextorNumber = input("Would you like to edit the (I)tems on your list or the (N)umber?")
        if TextorNumber.lower == "n":
            NewText = input(List1Number)
            List1Number = NewText
    elif ListSelection == List2:
        NewText = input(List2Number)
        List2Number = NewText
    elif ListSelection == List3:
        NewText = input(List3Number)
        List3Number = NewText
    elif ListSelection == List4:
        NewText = input(List4Number)
        List4Number = NewText
    elif ListSelection == List5:
        NewText = input(List5Number)
        List5Number = NewText
    elif ListSelection == "Back":
        Welcome()
    else:
        print("Please make sure to write one of the valid List names.")
        time.sleep(3)
        EditList()
    #Fetch List list and List, print List, make editable
    time.sleep(3)
    Welcome()
"""
def ViewList():
    global List1
    global List2
    global List3
    global List4
    global List5
    global List1
    global List2
    global List3
    global List4
    global List5
    global List1Items
    global List2Items
    global List3Items
    global List4Items
    global List5Items
    if List1 != ["ListName", "ListText"]:
        print(List1[1])
    if List2 != ["ListName", "ListText"]:
        print(List2[1])
    if List3 != ["ListName", "ListText"]:
        print(List3[1])
    if List4 != ["ListName", "ListText"]:
        print(List4[1])
    if List5 != ["ListName", "ListText"]:
        print(List5[1])
    ListSelection = input("Please input the name of the List you would like to view, or input 'Back' to go back.")
    if ListSelection == List1Name:
        print(List1[2])
        Back = input("Input anything when you are done viewing.")
    elif ListSelection == List2Name:
        print(List2[2])
        Back = input("Input anything when you are done viewing.")
    elif ListSelection == List3Name:
        print(List3[2])    
        Back = input("Input anything when you are done viewing.")
    elif ListSelection == List4Name:
        print(List4[2])
        Back = input("Input anything when you are done viewing.")
    elif ListSelection == List5Name:
        print(List5[2])
        Back = input("Input anything when you are done viewing.")
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

def DeleteList():
    global List1
    global List2
    global List3
    global List4
    global List5
    global List1
    global List2
    global List3
    global List4
    global List5
    global List1Items
    global List2Items
    global List3Items
    global List4Items
    global List5Items
    if List1 != ["ListName", "ListText"]:
        print(List1[1])
    if List2 != ["ListName", "ListText"]:
        print(List2[1])
    if List3 != ["ListName", "ListText"]:
        print(List3[1])
    if List4 != ["ListName", "ListText"]:
        print(List4[1])
    if List5 != ["ListName", "ListText"]:
        print(List5[1])
    ListSelection = input("Please input the name of the List you would like to delete, or input 'Back' to go back.")
    if ListSelection == List1Name:
        print(List1[2])
        Sure = input("Are you sure you want to delete this List? Input N for no and Y for yes.")
        if Sure == "Y":
            List1 = ["ListName", "ListText"]
            print("Deleting List...")
        elif Sure == "N":
            Continue = ""
    elif ListSelection == List2Name:
        print(List2[2])
        Sure = input("Are you sure you want to delete this List? Input N for no and Y for yes.")
        if Sure == "Y":
            List2 = ["ListName", "ListText"]
            print("Deleting List...")
        elif Sure == "N":
            Continue = ""
    elif ListSelection == List3Name:
        print(List3[2])
        Sure = input("Are you sure you want to delete this List? Input N for no and Y for yes.")
        if Sure == "Y":
            List3 = ["ListName", "ListText"]
            print("Deleting List...")
        elif Sure == "N":
            Continue = ""
    elif ListSelection == List4Name:
        print(List4[2])
        Sure = input("Are you sure you want to delete this List? Input N for no and Y for yes.")
        if Sure == "Y":
            List4 = ["ListName", "ListText"]
            print("Deleting List...")
        elif Sure == "N":
            Continue = ""
    elif ListSelection == List5Name:
        print(List5[2])
        Sure = input("Are you sure you want to delete this List? Input N for no and Y for yes.")
        if Sure == "Y":
            List5 = ["ListName", "ListText"]
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
    import passkey

def Welcome():
    global Selection
    print("Welcome to your Lists!")
    Selection = input("Write 'C' if you would like to create a List," '\n'
                  "write 'E' if you would like to edit an existing List," '\n'
                  "write 'V' if you would like to view an existing List," '\n'
                  "write 'D' if you would like to delete an existing List," '\n'
                  "or write 'L' if you would like to log out.")
    if Selection.lower == "c":
        CreateList()
    elif Selection.lower == "e":
        EditList()
    elif Selection.lower == "v":
        ViewList()
    elif Selection.lower == "d":
        DeleteList()
    elif Selection.lower == "l":
        Logout()
    else:
        "Please make sure to input one of the available options."
        time.sleep(3)
        Welcome()

Welcome()