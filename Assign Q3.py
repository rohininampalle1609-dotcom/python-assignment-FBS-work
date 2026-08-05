

def reverse(num, rev):
    if num == 0:
        return rev
    return reverse(num // 10, rev * 10 + num % 10)

n = int(input("Enter number: "))
print("Reverse =", reverse(n, 0))