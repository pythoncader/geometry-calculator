def calc():
  try:
    import myfunctions
    import sys

    myfunctions.clear()
    print('Find the Area of a Trapezoid \n\nPlease Type the First Base Length Below:')
    base1 = float(input())
    print('\nPlease Type the Second Base Length Below:')
    base2 = float(input())
    print('\nPlease Type the Height Below:')
    height = float(input())
    bases = base1+base2
    Area = 0.5 * height * bases
    print(f"\nHere is the area of your trapezoid: {Area}")
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