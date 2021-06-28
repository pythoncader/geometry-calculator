def calc():
  try:
    import sys
    import myfunctions

    myfunctions.clear()
    print("Find The Area Of A Triangle! (with base and height)")
    print("Make sure to type the base length first, then the height")
    print("\nType the base length here:")
    b = float(input())
    print("\nType the height here:")
    h = float(input())
    Area = (1 / 2 * b * h)
    print("\nAnd there is your answer!")
    print(Area)
    #start calculator again on keypress Enter	
    myfunctions.runmainagain()
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