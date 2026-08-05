

def armstrong(num, digits):
    if num == 0:
        return 0
    digit = num % 10
    return (digit ** digits) + armstrong(num // 10, digits)

n = int(input("Enter number: "))
digits = len(str(n))

if armstrong(n, digits) == n:
    print("Armstrong Number")
else:
    print("Not Armstrong Number")