

def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

def sum_factorial(n):
    if n == 1:
        return factorial(1)
    return factorial(n) + sum_factorial(n - 1)

n = int(input("Enter n: "))
print("Sum =", sum_factorial(n))