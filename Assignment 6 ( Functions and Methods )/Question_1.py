import math

def area_circle(radius):
    return math.pi * radius ** 2

def area_square(side):
    return side ** 2

def area_rectangle(length, width):
    return length * width

def area_triangle(base, height):
    return 0.5 * base * height

while True:
    print("\nChoose a shape to calculate the area:")
    print("1. Circle")
    print("2. Square")
    print("3. Rectangle")
    print("4. Triangle")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        radius = float(input("Enter the radius of the circle: "))
        print("The area of the circle is:", area_circle(radius))

    elif choice == '2':
        side = float(input("Enter the side length of the square: "))
        print("The area of the square is:", area_square(side))

    elif choice == '3':
        length = float(input("Enter the length of the rectangle: "))
        width = float(input("Enter the width of the rectangle: "))
        print("The area of the rectangle is:", area_rectangle(length, width))

    elif choice == '4':
        base = float(input("Enter the base length of the triangle: "))
        height = float(input("Enter the height of the triangle: "))
        print("The area of the triangle is:", area_triangle(base, height))

    elif choice == '5':
        print("Exiting the program.")
        break

    else:
        print("Invalid choice! Please enter a number from 1 to 5.")
