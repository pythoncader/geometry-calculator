def calc():
  try:
    import sys
    from tools import myfunctions
    import math

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
    Area = math.sqrt(xroot)

    text = "\nAnd there is your answer:"
    answer = Area
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