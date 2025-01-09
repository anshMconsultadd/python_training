import math

def calculate_area_and_perimeter():
    try:
        shape = input("Enter the shape").lower()

        if shape == "square":
            side = float(input("Enter the side length: "))
            area = side ** 2
            perimeter = 4 * side
            print(f"Area: {area}, Perimeter: {perimeter}")

        elif shape == "rectangle":
            length = float(input("Enter the length: "))
            width = float(input("Enter the width: "))
            area = length * width
            perimeter = 2 * (length + width)
            print(f"Area: {area}, Perimeter: {perimeter}")

        elif shape == "parallelogram":
            base = float(input("Enter the base length: "))
            height = float(input("Enter the height: "))
            side = float(input("Enter the side length: "))
            area = base * height
            perimeter = 2 * (base + side)
            print(f"Area: {area}, Perimeter: {perimeter}")

        elif shape == "triangle":
            base = float(input("Enter the base length: "))
            height = float(input("Enter the height: "))
            side1 = float(input("Enter side 1 length: "))
            side2 = float(input("Enter side 2 length: "))
            area = 0.5 * base * height
            perimeter = side1 + side2 + base
            print(f"Area: {area}, Perimeter: {perimeter}")

        elif shape == "circle":
            radius = float(input("Enter the radius: "))
            area = math.pi * (radius ** 2)
            perimeter = 2 * math.pi * radius
            print(f"Area: {area}, Perimeter: {perimeter}")

        else:
            print("Invalid shape entered!")
    except :
        print("Invalid input! Please enter numeric values.")

calculate_area_and_perimeter()
