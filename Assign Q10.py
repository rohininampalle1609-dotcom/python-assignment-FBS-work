# reverse of a number

def reverse(num):
    rev = 0

    while num > 0:
        digit = num % 10
        rev = rev * 10 + digit
        num //= 10

    return rev

n = int(input("Enter number: "))
print("Reverse =", reverse(n))