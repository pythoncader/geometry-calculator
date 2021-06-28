def calc():
  try:
    print('running perimeter...')
    import sys
    import myfunctions

    myfunctions.clear()
    print("What would you like to calculate? \n '1' = polygon perimeter (3 to 15 sides)\n '2' = circle circumference or area\n ...")
    try:
      calculate = int(input())
    except Exception:
      myfunctions.invalidinput()
      return

    if calculate == 1:
        import Perimetercalc
        Perimetercalc.calc()
        return
    elif calculate == 2:
        import CircumferenceAreaCirclecalc
        CircumferenceAreaCirclecalc.calc()
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