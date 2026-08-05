

def power(m, n):
    if n == 0:
        return 1
    return m * power(m, n - 1)

m = int(input("Enter base: "))
n = int(input("Enter exponent: "))

print("Result =", power(m, n))