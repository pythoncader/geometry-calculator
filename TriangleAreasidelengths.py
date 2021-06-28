def calc():
  try:
    import sys
    import myfunctions

    myfunctions.clear()
    print("Find The Area Of A Triangle! (with side lengths)")
    print("\nType the first side length here:")
    a = float(input())
    print("\nType the second side length here:")
    b = float(input())
    print("\nType the third side length here:")
    c = float(input())
    sa = 0.5 * a
    sb = 0.5 * b
    sc = 0.5 * c
    s = sa + sb + sc
    xroot = s * (s-a)*(s-b)*(s-c)
    import math
    Area = math.sqrt(xroot)
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