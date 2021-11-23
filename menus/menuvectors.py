def calc():
  try:
    print("running vectors...")
    import sys
    from tools import myfunctions
    from calculators import vectorcomponents, vectorinfo, vectorsubtraction, vectoraddition, vectorangle

    myfunctions.clear()
    print("What would you like to calculate? \n '1' = find components of vector \n '2' = vector magnitude and direction \n '3' = subtraction of vectors \n '4' = addition of vectors \n '5' = dot product and angle between vectors \n ...")
    try:
      calculate = int(input())
    except Exception:
      myfunctions.invalidinput()
      return

    if calculate == 1:
        text, answer = vectorcomponents.calc()
        return text, answer
    elif calculate == 2:
        text, answer = vectorinfo.calc()
        return text, answer
    elif calculate == 3:
        text, answer = vectorsubtraction.calc()
        return text, answer
    elif calculate == 4:
        text, answer = vectoraddition.calc()
        return text, answer
    elif calculate == 5:
        text, answer = vectorangle.calc()
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