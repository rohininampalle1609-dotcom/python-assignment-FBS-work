# Wap to check whether the triangle is equilatral , isosceles or scalene triangle.



side1 = float(input("Enter first side: "))
side2 = float(input("Enter second side: "))
side3 = float(input("Enter third side: "))

# First check if the triangle is valid
if (side1 + side2 > side3) and (side1 + side3 > side2) and (side2 + side3 > side1):

    if side1 == side2 == side3:
        print("Equilateral Triangle")

    elif side1 == side2 or side1 == side3 or side2 == side3:
        print("Isosceles Triangle")

    else:
        print("Scalene Triangle")

else:
    print("Invalid Triangle")