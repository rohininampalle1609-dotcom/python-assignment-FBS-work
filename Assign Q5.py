# sum of series(11 +22+33+......+nn)


def power_sum(n):
    total = 0
    for i in range(1, n + 1):
        total += i ** i
    return total

n = int(input("Enter n: "))
print("Sum =", power_sum(n))