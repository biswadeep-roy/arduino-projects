#----------------------------------------------
#            GEOMETRIC SHAPE AREAS
#            ======================
#
# This program calculates and displays the areas
# of various geometrical shapes based on user input.
#
# Author: Biswadeep Roy
# File  : geometric_areas.py
#----------------------------------------------
import math

def calculate_square_area(side):
    return side * side

def calculate_rectangle_area(length, width):
    return length * width

def calculate_triangle_area(base, height):
    return 0.5 * base * height

def calculate_circle_area(radius):
    return math.pi * radius * radius

def calculate_cylinder_area(radius, height):
    return 2 * math.pi * radius * height

print("GEOMETRIC SHAPE AREAS")
print("=====================\n")

print("Select the shape to calculate its area:")
shape = input("Square (s)\nRectangle (r)\nCircle (c)\nTriangle (t)\nCylinder (y): ").lower()

if shape == 's':
    side = float(input("Enter the side length of the square: "))
    area = calculate_square_area(side)
    shape_name = "Square"
elif shape == 'r':
    length = float(input("Enter the length of the rectangle: "))
    width = float(input("Enter the width of the rectangle: "))
    area = calculate_rectangle_area(length, width)
    shape_name = "Rectangle"
elif shape == 'c':
    radius = float(input("Enter the radius of the circle: "))
    area = calculate_circle_area(radius)
    shape_name = "Circle"
elif shape == 't':
    base = float(input("Enter the base length of the triangle: "))
    height = float(input("Enter the height of the triangle: "))
    area = calculate_triangle_area(base, height)
    shape_name = "Triangle"
elif shape == 'y':
    radius = float(input("Enter the radius of the cylinder: "))
    height = float(input("Enter the height of the cylinder: "))
    area = calculate_cylinder_area(radius, height)
    shape_name = "Cylinder"
else:
    area = None
    shape_name = None
    print("Invalid shape selected.")

if area is not None:
    print(f"The area of the {shape_name} is {area:.2f}")
