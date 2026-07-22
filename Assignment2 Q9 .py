# Write a program to swap two numbers without third variable.

a =int(input("Enter first number:"))
b =int(input("Enter second number:"))

print("before swapping:")
print("a =", a)
print(" b =",b)

a = a + b
b = a - b
a = a - b

print("after swapping:")
print("a =", a)
print(" b =",b)