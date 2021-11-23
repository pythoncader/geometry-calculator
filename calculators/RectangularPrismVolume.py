def calc():
  try:
    from tools import myfunctions
    import sys

    myfunctions.clear()
    print('Find the volume of a rectangular prism:')
    print('\nWrite the length here (in feet, decimals if not integer):')
    lfeet = float(input())
    lyards = lfeet/3
    print('\nWrite the width here (in feet, decimals if not integer):')
    wfeet = float(input())
    wyards = wfeet/3
    print('\nWrite the height here (in feet, decimals if not integer):')
    hfeet = float(input()) 
    hyards = hfeet/3

    volume=lyards*wyards*hyards

    text = f"\nHere is the volume of your rectangular prism: {volume} cubic yards or {lfeet*wfeet*hfeet} cubic feet"
    return text, ""

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