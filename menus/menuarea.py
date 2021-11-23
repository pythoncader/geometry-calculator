def calc():
  try:
    print("running area...")
    import sys
    from tools import myfunctions
    from calculators import TriangleAreabaseheight, TriangleAreasidelengths, CircleArea, TrapezoidAreacalc

    myfunctions.clear()
    print("What would you like to calculate? \n '1' = triangle area (with base and height)\n '2' = triangle area (with side lengths)\n '3' = circle area\n '4' = trapezoid area\n ...")
    try:
      calculate = int(input())
    except Exception:
      myfunctions.invalidinput()
      return

    if calculate == 1:
        text, answer = TriangleAreabaseheight.calc()
        return text, answer
    elif calculate == 2:
        text, answer = TriangleAreasidelengths.calc()
        return text, answer
    elif calculate == 3:
        text, answer = CircleArea.calc()
        return text, answer
    elif calculate == 4:
        text, answer = TrapezoidAreacalc.calc()
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