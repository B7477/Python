## N-sided Polygon class definition and main function##

# Description: In this program, we are using a class and function to calculate the perimeter and area of of a polygon. To calculate these values, the user will be prompted 
    # to type a number of sides and length of sides value within a specific limit. Then the program will calculate wanted values. This program uses class-def methods of python



import math

class Polygon:
    
    def __init__(self):
        self.__numSides = 0
        self.__lenSides = 0.0

    def getNumSides(self):
        return self.__numSides
    
    def getLenSides(self):
        return self.__lenSides

    def setNumSides(self, n):
        self.__numSides = n
        
    def setLenSides(self, l):
        self.__lenSides = l

    def perimeter(self):
        perim = (self.__numSides * self.__lenSides)
        print(f'The perimeter of the polygon is {perim:.3f} units.')
        
    def area(self):
        area = ((self.__numSides*(self.__lenSides**2))/(4*(math.tan(math.pi/self.__numSides))))
        print(f"The area of the polygon is {area:.3f} square units.")

def main():
    polygon = Polygon()
    
    num = int(input('Enter the number of sides (>=3): '))
    if num < 3:
        num = int(input('Invalid. Enter the number of sides (>=3): '))
    polygon.setNumSides(num)
        
    length = float(input('Enter the length of each sides (>= 0.1): '))
    if length < 0.1:
        length = float(input('Invalid. Enter the length of each sides (>= 0.1): '))
    polygon.setLenSides(length)

    print(f'The polygon has {num} sides. Each side is {length} units in length.')

    polygon.perimeter()
    polygon.area()

main()




    
