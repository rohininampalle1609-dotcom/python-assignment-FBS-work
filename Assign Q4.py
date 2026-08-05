# sum of factorial(1!+ 2!=.....+n)


def factorial(num):
    fact = 1
    for i in range(1, num + 1):
        fact *= i
    return fact

def sum_factorial(n):
    total = 0
    for i in range(1, n + 1):
        total += factorial(i)
    return total

n = int(input("Enter n: "))
print("Sum =", sum_factorial(n))