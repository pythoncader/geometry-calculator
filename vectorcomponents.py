def calc():
    try:
        import myfunctions
        import sys

        myfunctions.clear()
        print("Find the components of a vector with its tail and head points:")
        
        xt = float(input("\nPlease enter the x value of the starting point or tail of the vector:\n"))
        yt = float(input("\nPlease enter the y value of the starting point or tail of the vector:\n"))
        xh = float(input("\nPlease enter the x value of the ending point or head of the vector:\n"))
        yh = float(input("\nPlease enter the y value of the ending point or head of the vector:\n"))

        
        newx = xh - xt
        newy = yh - yt

        print(f"\n\nHere are the components of the vector: ({newx}, {newy})")

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