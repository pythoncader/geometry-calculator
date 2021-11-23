def calc():
  try:
    from tools import myfunctions
    import sys

    myfunctions.clear()
    pi = 3.1415926535897932384626433832795
    
    myfunctions.clear()
    #Circle Circumference Calculation
    print("Find the circumference of a circle\n")
    print("Write the radius here: ")
    radius = float(input())

    text = "\nHere is Your Circle's Circumference:"
    answer = radius * 2 * pi
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