def calc():
    try:
        import myfunctions
        import sys

        myfunctions.clear()
        print("Subtract the second vector from the first:")
        
        x1 = float(input("\nPlease enter the x value of the first vector's components:\n"))
        y1 = float(input("\nPlease enter the y value of the first vector's components:\n"))
        x2 = float(input("\nPlease enter the x value of the second vector's components:\n"))
        y2 = float(input("\nPlease enter the y value of the second vector's components:\n"))

        
        newx = x1 - x2
        newy = y1 - y2

        print(f"\n\n({x1}, {y1}) - ({x2}, {y2}) = ({newx}, {newy})")

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