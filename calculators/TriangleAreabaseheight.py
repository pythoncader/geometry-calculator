def calc():
  try:
    import sys
    from tools import myfunctions

    myfunctions.clear()
    print("Find The Area Of A Triangle! (with base and height)")
    print("\nType the base length here:")
    b = float(input())
    print("\nType the height here:")
    h = float(input())
    Area = (0.5 * b * h)

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