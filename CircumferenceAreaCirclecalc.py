def calc():
  try:
    import myfunctions
    import sys

    myfunctions.clear()
    pi = 3.1415926535897932384626433832795
    print('Find the Circumference or Area of a Circle:')
    print(" '1' = circumference \n '2' = area\n ...")
    try:
      CircorArea = int(input())
    except Exception:
      myfunctions.invalidinput()
      return
      
    if CircorArea == 1:
      myfunctions.clear()
      #CircumferenceCalculation
      print("Find the circumference of a circle\n")
      print("Write the radius here: ")
      radiuscirc = float(input())
      Circumference = radiuscirc * 2 * pi
      print("\nHere is Your Circle's Circumference: \n" +str(Circumference))
    elif CircorArea == 2:
      myfunctions.clear()
      print("Find the area of a circle\n")
      print("Write the radius here: ")
      radiusarea = float(input())
      print("\nHere is Your Circle's Area:")
      print(radiusarea * radiusarea * pi)
    else:
      print("Entry is not valid")
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