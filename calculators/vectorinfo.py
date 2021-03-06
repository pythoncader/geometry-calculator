def calc():
    try:
        from calculators.distancebetweenpointsformula import finddistance
        import math
        from tools import myfunctions
        import sys

        myfunctions.clear()
        print("Find the magnitude and direction of a vector with its components:")
        
        x1 = float(input("\nPlease enter the x value of the vector's components:\n"))
        y1 = float(input("\nPlease enter the y value of the vector's components:\n"))

        if y1 < 0 and x1 > 0:
            quadrant = 4
        elif y1 < 0 and x1 < 0:
            quadrant = 3
        elif y1 > 0 and x1 < 0:
            quadrant = 2
        elif y1 > 0 and x1 > 0:
            quadrant = 1
        elif y1 == 0 and x1 > 0:
            quadrant = 5
        elif x1 == 0 and y1 > 0:
            quadrant = 6
        elif y1 == 0 and x1 < 0:
            quadrant = 7
        elif x1 == 0 and y1 < 0:
            quadrant = 8
        elif y1 == 0 and x1 == 0:
            text = "\nNot a vector - starting and ending points are the same"
            return text, ""

        v_magnitude, inside = finddistance(0, 0, x1, y1)

        if quadrant != 6 and quadrant != 8:
            slope = y1/x1
        else:
            slope = "undefined"
        
        if quadrant == 1:
            vector_quadrant = "\n\nThe vector points into quadrant I"
            angle_deg = math.degrees(math.atan(abs(slope)))
            angle_rad = math.radians(angle_deg)
        elif quadrant == 2:
            vector_quadrant = "\n\nThe vector points into quadrant II"
            angle_deg = 180 - math.degrees(math.atan(abs(slope)))
            angle_rad = math.radians(angle_deg)
        elif quadrant == 3:
            vector_quadrant = "\n\nThe vector points into quadrant III"
            angle_deg = 180 + math.degrees(math.atan(abs(slope)))
            angle_rad = math.radians(angle_deg)
        elif quadrant == 4:
            vector_quadrant = "\n\nThe vector points into quadrant IV"
            angle_deg = 360 - math.degrees(math.atan(abs(slope)))
            angle_rad = math.radians(angle_deg)
        elif quadrant == 5:
            vector_quadrant = "\n\nThe vector points straight right"
            angle_deg = 0
            angle_rad = math.radians(angle_deg)
        elif quadrant == 6:
            vector_quadrant = "\n\nThe vector points straight up"
            angle_deg = 90
            angle_rad = math.radians(angle_deg)
        elif quadrant == 7:
            vector_quadrant = "\n\nThe vector points straight left"
            angle_deg = 180
            angle_rad = math.radians(angle_deg)
        elif quadrant == 8:
            vector_quadrant = "\n\nThe vector points straight down"
            angle_deg = 270
            angle_rad = math.radians(angle_deg)

        text = f"{vector_quadrant}\n\nThe vector's magnitude is {v_magnitude} or ???{inside}\n\nThe slope of the vector is {slope}\n\nThe vector's direction is {angle_deg} degrees or {angle_rad} radians"
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