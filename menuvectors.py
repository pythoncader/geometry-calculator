def calc():
  try:
    print("running vectors...")
    import sys
    import myfunctions

    myfunctions.clear()
    print("What would you like to calculate? \n '1' = find components of vector \n '2' = vector magnitude and direction \n '3' = subtraction of vectors \n '4' = addition of vectors \n '5' = dot product and angle between vectors \n ...")
    try:
      calculate = int(input())
    except Exception:
      myfunctions.invalidinput()
      return

    if calculate == 1:
        import vectorcomponents
        vectorcomponents.calc()
        return
    elif calculate == 2:
        import vectorinfo
        vectorinfo.calc()
        return
    elif calculate == 3:
        import vectorsubtraction
        vectorsubtraction.calc()
        return
    elif calculate == 4:
        import vectoraddition
        vectoraddition.calc()
        return
    elif calculate == 5:
        import vectorangle
        vectorangle.calc()
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