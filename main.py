try:
  import myfunctions
  import sys
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
        import menuvolume
        menuvolume.calc()
    elif calculate == 2:
        import menuarea
        menuarea.calc()
    elif calculate == 3:
        import menuperimeter
        menuperimeter.calc()
    elif calculate == 4:
        import menufindingvalues
        menufindingvalues.calc()
    elif calculate == 5:
        import menuvectors
        menuvectors.calc()
    else:
        myfunctions.invalidinput()
  except Exception:
    print("Something went wrong!")
  except KeyboardInterrupt:
    myfunctions.clear()
    sys.exit("Quitting Geometry Calculator...")