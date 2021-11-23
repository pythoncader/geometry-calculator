def calc():
  try:
    print('running finding values...')
    import sys
    from tools import myfunctions
    from calculators import distancebetweenpointsformula, PythagoreanTheorem

    myfunctions.clear()
    print("What would you like to calculate? \n '1' = distance formula \n '2' = pythagorean theorem\n ...")
    try:
      calculate = int(input())
    except Exception:
      myfunctions.invalidinput()
      return

    if calculate == 1:
        text, answer = distancebetweenpointsformula.calc()
        return text, answer
    elif calculate == 2:
        text, answer = PythagoreanTheorem.calc()
        return text, answer
        
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