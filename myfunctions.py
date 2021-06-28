def clear():
    try:
        import replit
        replit.clear()
        print("You are using replit\n")
    except Exception:
        import os
        returnvalue = os.system("cls")
        print("You are using a Windows PC\n")
        if returnvalue != 0:
            os.system("clear")
            print("You are using OSX or Linux\n")

def runmainagain():
  print('\n\nPress enter to calculate again or CTRL + C to quit')
  input("")
  
def invalidinput():
  clear()
  print('Input not valid.\n\nPress enter to calculate again or CTRL + C to quit')
  input("")