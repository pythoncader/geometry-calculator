def calc():
	try:
		import math
		import sys
		from tools import myfunctions

		myfunctions.clear()
		print("What would you like to calculate? \n '1' = missing side length\n '2' = right triangle verification\n ...")
		try:
			calculate = int(input())
		except Exception:
			myfunctions.invalidinput()
			return

		if calculate == 1:
			myfunctions.clear()
			print('Find the missing side length of a triangle: c = hypotenuse, b = leg, a = other leg. \nSimply put the missing side length in as 0 (zero)')
			a = float(input("\nWrite the value of side a:\n"))
			b = float(input("\nWrite the value of side b:\n"))
			c = float(input("\nWrite the value of side c:\n"))

			if a == 0:
				bsqrd = b * b
				csqrd = c * c
				asqrd = csqrd - bsqrd
				a = math.sqrt(asqrd)

				text = "\n\nThe side length a is equal to:"
				answer = a
				return text, answer
			elif b == 0:
				asqrd = a * a
				csqrd = c * c
				bsqrd = csqrd - asqrd
				b = math.sqrt(bsqrd)

				text = "\n\nThe side length b is equal to:"
				answer = b
				return text, answer
			elif c == 0:
				asqrd = a * a
				bsqrd = b * b
				csqrd = asqrd + bsqrd
				c = math.sqrt(csqrd)

				text = "\n\nThe side length c is equal to:"
				answer = c
				return text, answer
			
			

		elif calculate == 2:
			myfunctions.clear()
			print('Find out if a triangle is a right triangle or not based on the side lengths:\nc = hypotenuse or longest side, b = leg or any other side, a = other leg\n\nPlease type the length of side c below: (as an integer or decimal)')
			sidec = float(input())
			print('\nPlease type the length of side b below:')
			sideb = float(input())
			print('\nPlease type the length of side a below:')
			sidea = float(input())
			asqrd = sidea * sidea
			bsqrd = sideb * sideb
			csqrd = sidec * sidec
			aplsbsqrd = asqrd + bsqrd
			csqrdstr = str(csqrd) #converts c squared to a string for subscripting
			roundedaplsbsqrd = round(aplsbsqrd, csqrdstr[::-1].find('.')) #rounds the value to the same amount of decimal places as are in c squared
			if aplsbsqrd == csqrd:
				text = '\nYour triangle, with side lengths a = '+str(sidea)+" b = "+str(sideb)+" and c = "+str(sidec)+" is a right triangle"
				return text, ""
			elif roundedaplsbsqrd == csqrd:
				text = '\nIt is a right triangle, but it is close:\n\nc squared is equal to: '+str(csqrd)+ ", and b squared plus a squared is equal to: "+str(aplsbsqrd)
				return text, ""
			else:
				text = '\nNope, this triangle is not a right triangle: \n\nc squared is equal to: '+str(csqrd)+ ', and b squared plus a squared is equal to: '+str(aplsbsqrd)
				return text, ""
		else:
			myfunctions.invalidinput()
			return "", ""
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