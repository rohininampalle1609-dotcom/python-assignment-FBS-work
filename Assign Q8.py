

def is_prime(num, i=2):
    if num < 2:
        return False
    if i * i > num:
        return True
    if num % i == 0:
        return False
    return is_prime(num, i + 1)

n = int(input("Enter number: "))

if is_prime(n):
    print("Prime Number")
else:
    print("Not Prime Number")