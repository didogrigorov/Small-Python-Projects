import math

geometry_type = input("Enter square, rectangle, circle or triangle: ")

if geometry_type == "square":
    side = float(input("Enter the length of the side: "))
    area = side * side
    print(f"Area is {area:.3f}")
elif geometry_type == "rectangle":
    length1 = float(input("Enter the length of the side 1: "))
    length2 = float(input("Enter the length of the side 2: "))
    area = length1 * length2
    print(f"Area is {area:.3f}")
elif geometry_type == "circle":
    radius = float(input("Enter the length of the radius: "))
    area = radius ** 2 * math.pi
    print(f"Area is {area:.3f}")
elif geometry_type == "triangle":
    length_side = float(input("Enter length of the side: "))
    length_height = float(input("Enter length of the height: "))
    area = (length_side * length_height) / 2
    print(f"Area is {area:.3f}")
else:
    print("Wrong choice!")
