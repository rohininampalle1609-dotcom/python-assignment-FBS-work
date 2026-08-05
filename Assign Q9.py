# sum of digits of a number


def digit_sum(num):
    total = 0

    while num > 0:
        total += num % 10
        num //= 10

    return total

n = int(input("Enter number: "))
print("Sum of Digits =", digit_sum(n))