def calc():
  try:
    print('running perimeter...')
    import sys
    from tools import myfunctions
    from calculators import Perimetercalc, CircleCircumference

    myfunctions.clear()
    print("What would you like to calculate? \n '1' = polygon perimeter (3 to 15 sides)\n '2' = circle circumference\n ...")
    try:
      calculate = int(input())
    except Exception:
      myfunctions.invalidinput()
      return

    if calculate == 1:
        text, answer = Perimetercalc.calc()
        return text, answer
    elif calculate == 2:
        text, answer = CircleCircumference.calc()
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