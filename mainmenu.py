import time
Lists = []
Selection = ""
List1 = ("")
List1Number = ["ListNumber"]
List2 = ("ListName")
List2Number = ["ListNumber"]
List3 = ("ListName")
List3Number = ["ListName"]
List4 = ("ListName")
List4Number = ["ListName"]
List5 = ("ListName")
List5Number = ["ListName"]

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
        List1Number = ListText
        print("Saving List...")
    elif List2 == ["ListName", "ListText"]:
        List2[1] = str(TempListName)
        List2[2] = str(ListText)
        print("Saving List...")
    elif List3 == ["ListName", "ListText"]:
        List3[1] = str(TempListName)
        List3[2] = str(ListText)
        print("Saving List...")
    elif List4 == ["ListName", "ListText"]:
        List4[1] = str(TempListName)
        List4[2] = str(ListText)
        print("Saving List...")
    elif List5 == ["ListName", "ListText"]:
        List5[1] = str(TempListName)
        List5[2] = str(ListText)
        print("Saving List...")
    else:
        print("Out of space, please delete a List to continue.")
    #Save List Text to Database
    time.sleep(3)
    Welcome()

def EditList():
    global ListList
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
    ListSelection = input("Please input the name of the List you would like to edit, or input 'Back' to go back.")
    if ListSelection == List1Name:
        NewText = input(List1[2])
        List1[2] = NewText
    elif ListSelection == List2Name:
        NewText = input(List2[2])
        List2[2] = NewText
    elif ListSelection == List3Name:
        NewText = input(List3[2])
        List3[2] = NewText
    elif ListSelection == List4Name:
        NewText = input(List4[2])
        List4[2] = NewText
    elif ListSelection == List5Name:
        NewText = input(List5[2])
        List5[2] = NewText
    elif ListSelection == "Back":
        Continue = ""
    else:
        print("Please make sure to write one of the valid List names.")
        time.sleep(3)
        EditList()
    #Fetch List list and List, print List, make editable
    time.sleep(3)
    Welcome()

def ViewList():
    global ListList
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
    global ListList
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
    if Selection == "C":
        CreateList()
    elif Selection == "E":
        EditList()
    elif Selection == "V":
        ViewList()
    elif Selection == "D":
        DeleteList()
    elif Selection == "L":
        Logout()
    else:
        "Please make sure to input one of the available options."
        time.sleep(3)
        Welcome()

Welcome()