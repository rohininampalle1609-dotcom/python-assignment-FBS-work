# Armstrong number

def armstrong(num):
    temp = num
    digits = len(str(num))
    total = 0

    while temp > 0:
        digit = temp % 10
        total += digit ** digits
        temp //= 10

    return total == num

n = int(input("Enter number: "))

if armstrong(n):
    print("Armstrong Number")
else:
    print("Not Armstrong Number")