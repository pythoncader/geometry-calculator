def calc():
	try:
		import math
		import sys
		import myfunctions

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
				print(f"\n\nThe side length a is equal to: {a}")
			elif b == 0:
				asqrd = a * a
				csqrd = c * c
				bsqrd = csqrd - asqrd
				b = math.sqrt(bsqrd)
				print(f"\n\nThe side length b is equal to: {b}")
			elif c == 0:
				asqrd = a * a
				bsqrd = b * b
				csqrd = asqrd + bsqrd
				c = math.sqrt(csqrd)
				print(f"\n\nThe side length c is equal to: {c}")
			
			

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
				print('\nYour triangle, with side lengths a = '+str(sidea)+" b = "+str(sideb)+" and c = "+str(sidec)+" is a right triangle")
			elif roundedaplsbsqrd == csqrd:
				print('\nIt is a right triangle, but it is close:\n\nc squared is equal to: '+str(csqrd)+ ", and b squared plus a squared is equal to: "+str(aplsbsqrd))
			else:
				print('\nNope, this triangle is not a right triangle: \n\nc squared is equal to: '+str(csqrd)+ ', and b squared plus a squared is equal to: '+str(aplsbsqrd))
		else:
			print('Input not valid')
	#except Exception:
		#print("Something went wrong!")
	except KeyboardInterrupt:
		myfunctions.clear()
		sys.exit("Quitting Geometry Calculator...")
	#start calculator again on keypress Enter
	myfunctions.runmainagain()
	return
  
if __name__ == "__main__":
  calc()