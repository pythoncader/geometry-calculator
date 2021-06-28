def calc():
    try:
        from distancebetweenpointsformula import finddistance
        import math
        import myfunctions
        import sys

        myfunctions.clear()
        print("Find the dot product and angle between two vectors:")

        x1 = float(input("\nPlease enter the x value of the first vector's components:\n"))
        y1 = float(input("\nPlease enter the y value of the first vector's components:\n"))
        x2 = float(input("\nPlease enter the x value of the second vector's components:\n"))
        y2 = float(input("\nPlease enter the y value of the second vector's components:\n"))


        xs = x1 * x2
        ys = y1 * y2

        dot_product = xs + ys
        print(f"\n\nThe dot product of the vectors is {dot_product}")

        v1_magnitude = finddistance(0, 0, x1, y1)
        v2_magnitude = finddistance(0, 0, x2, y2)

        cosine_of_angle = (dot_product/v1_magnitude)/v2_magnitude
        angle_between_vectors = math.acos(cosine_of_angle)

        print(f"\n\nThe angle between the vectors is {math.degrees(angle_between_vectors)} degrees or {angle_between_vectors} radians")

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