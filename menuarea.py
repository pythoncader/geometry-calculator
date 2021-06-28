def calc():
  try:
    print("running area...")
    import sys
    import myfunctions

    myfunctions.clear()
    print("What would you like to calculate? \n '1' = triangle area (with base and height)\n '2' = triangle area (with side lengths)\n '3' = circle circumference or area\n '4' = trapezoid area\n ...")
    try:
      calculate = int(input())
    except Exception:
      myfunctions.invalidinput()
      return

    if calculate == 1:
        import TriangleAreabaseheight
        TriangleAreabaseheight.calc()
        return
    elif calculate == 2:
        import TriangleAreasidelengths
        TriangleAreasidelengths.calc()
        return
    elif calculate == 3:
        import CircumferenceAreaCirclecalc
        CircumferenceAreaCirclecalc.calc()
        return
    elif calculate == 4:
        import TrapezoidAreacalc
        TrapezoidAreacalc.calc()
        return
  #except Exception:
   # print("Something went wrong!")
  except KeyboardInterrupt:
    myfunctions.clear()
    sys.exit("Quitting Geometry Calculator...")
  #start calculator again on keypress Enter
  myfunctions.runmainagain()
  return
  
if __name__ == "__main__":
  calc()