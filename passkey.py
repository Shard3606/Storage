import time
Username = ""
Password = ""
UsernameGuess = ""
PasswordGuess = ""
AlreadyAccount = ""

def createaccount():
  global Username
  global Password
  Username = input("Please create a username, or input 'Back' to go back.")
  if Username == "Back":
    AlrAcc()
  else:
    #Save Username
    Password = input("Please create a password, or input 'Back' to go back.")
  if Password == "Back":
    AlrAcc()
  else:
    #Save Password, attach to username
    time.sleep(3)
    AlrAcc()

def signintoaccount():
  global Username
  global Password
  global UsernameGuess
  global PasswordGuess
  UsernameGuess = input("Please input your username, or input 'Back' to go back.")
  if UsernameGuess == "Back":
    AlrAcc()
  else:
    PasswordGuess = input("Please input your password, or input 'Back' to go back.")
  if Password == "Back":
    AlrAcc()
  else:
    #Check Database
    if UsernameGuess == Username and PasswordGuess == Password:
      Finish()
      time.sleep(3)
    else:
      print("Incorrect username or password. Please try again.")
      time.sleep(3)
      signintoaccount()

def AlrAcc():
  AlreadyAccount = input("Do you already have an account? Input Y for yes and N for no.")
  if AlreadyAccount == "Y":
    signintoaccount()
  elif AlreadyAccount == "N":
    createaccount()
  else:
    print("Please make sure you inputted Y or N.")
    time.sleep(3)
    AlrAcc()

def Finish():
  print("Welcome...")
  time.sleep(3)
  import mainmenu

if Username == "" and Password == "":
  AlrAcc()
else:
  signintoaccount()

AlrAcc()
