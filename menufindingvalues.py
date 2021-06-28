def calc():
  try:
    print('running finding values...')
    import sys
    import myfunctions

    myfunctions.clear()
    print("What would you like to calculate? \n '1' = distance formula \n '2' = pythagorean theorem\n ...")
    try:
      calculate = int(input())
    except Exception:
      myfunctions.invalidinput()
      return

    if calculate == 1:
        import distancebetweenpointsformula
        distancebetweenpointsformula.calc()
        return
    elif calculate == 2:
        import PythagoreanTheorem
        PythagoreanTheorem.calc()
        return
  except Exception:
    print("Something went wrong!")
  except KeyboardInterrupt:
    myfunctions.clear()
    sys.exit("Quitting Geometry Calculator...")
  #start calculator again on keypress Enter
  myfunctions.runmainagain()
  return
  
if __name__ == "__main__":
  calc()