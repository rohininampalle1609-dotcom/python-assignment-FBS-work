#x -x2/3+ x3/5-x4/7+.....up to n terms

x = int(input("Enter x: "))
n = int(input("Enter Number of Terms: "))

sum = 0
sign = 1
den = 1

for i in range(1, n + 1):
    sum = sum + sign * (x ** i) / den
    sign = sign * -1
    den = den + 2

print("Sum =", sum)