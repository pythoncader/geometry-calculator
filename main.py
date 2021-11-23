try:
  from tools import myfunctions
  import sys
  import pyperclip
  from menus import menuvolume, menuarea, menuperimeter, menufindingvalues, menuvectors
except:
  sys.exit("Imports failed")

while True:
  try:
    myfunctions.clear()
      
    print("What would you like to calculate? \n '1' = volume \n '2' = area \n '3' = perimeter \n '4' = finding values \n '5' = vectors \n ...")

    try:
      calculate = int(input())
    except Exception:
      myfunctions.invalidinput()
      continue

    if calculate == 1:
      print("hello world!")
      text, answer = menuvolume.calc()
    elif calculate == 2:
      text, answer = menuarea.calc()
    elif calculate == 3:
      text, answer = menuperimeter.calc()
    elif calculate == 4:
      text, answer = menufindingvalues.calc()
    elif calculate == 5:
      text, answer = menuvectors.calc()
    else:
      text, answer = myfunctions.invalidinput()

    if text != "":
      print(f"{text} {answer}")
      if answer != "":
        yesorno = input("\nCopy To Clipboard?\n")
        if "y" in yesorno or "s" in yesorno:
          pyperclip.copy(answer)
          print("\nCopied Successfully!")

    myfunctions.runmainagain()

  except Exception:
    print("Something went wrong!")
  except KeyboardInterrupt:
    myfunctions.clear()
    sys.exit("Quitting Geometry Calculator...")