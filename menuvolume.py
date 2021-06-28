def calc():
  try:
    print('running volume...')
    import sys
    import myfunctions

    myfunctions.clear()
    print("What would you like to calculate? \n '1' = rectangular prism volume\n ...")
    try:
      calculate = int(input())
    except Exception:
      myfunctions.invalidinput()
      return

    if calculate == 1:
        import RectangularPrismVolume
        RectangularPrismVolume.calc()
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