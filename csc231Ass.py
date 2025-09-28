# Name: Richard Otega Mark
# Level: 200
# Matric no.: E055424
# Course: csc231
class Area():
	def rectangle(self, l, b):
		return l * b
		
	def circle(self, r):
		return 3.141 * r**2
		
	def parallelogram(self, h, b):
		return h * b	
		
area = Area()

while True:
	print("\n ---=Area Calculator=---\n")
	action = input("Hi. What area will you like to calculate?\nEnter 'R', 'C', or 'P' for rectangle, circle or parallelogram: ").upper()
	if action == "R":
		while True:
			try:
				l = float(input("\nenter the length of your rectangle: "))
				b = float(input("enter the breadth of your rectangle: "))
				print(f"The area of your rectangle is: {round(area.rectangle(l, b), 3)}m²")
				break
			except ValueError:
				print("Please enter a valid number!")
	elif action == "C":
			while True:
				try:
					r = float(input("\nenter the radius of your circle: "))
					print(f"The area of your circle is: {round(area.circle(r), 3)}m²")
					break
				except ValueError:
					print("Please enter a valid number!")
					
	elif action == "P":
		while True:
			try:
				h = float(input("\nenter the height of your parallelogram: "))
				b = float(input("enter the base length of the parallelogram: "))
				print(f"The area of your parallelogram is: {round(area.parallelogram(h, b), 3)}m²")
				break
			except ValueError:
				print("Please enter a valid number!")
				
	else:
		print("Invalid Input!")

	
			