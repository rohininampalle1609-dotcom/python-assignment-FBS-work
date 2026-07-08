# program to find the Roots of the quadratic equation

import math

# Input coefficients
a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))

# Calculate the discriminant
d = b**2 - 4*a*c

# Check the nature of the roots
if d > 0:
    root1 = (-b + math.sqrt(d)) / (2 * a)
    root2 = (-b - math.sqrt(d)) / (2 * a)
    print("The roots are real and different.")
    print("Root 1 =", root1)
    print("Root 2 =", root2)

elif d == 0:
    root = -b / (2 * a)
    print("The roots are real and equal.")
    print("Root =", root)

else:
    real = -b / (2 * a)
    imaginary = math.sqrt(-d) / (2 * a)
    print("The roots are complex.")
    print("Root 1 =", real, "+", imaginary, "i")
    print("Root 2 =", real, "-", imaginary, "i")