# palindrome number


def reverse(num):
    rev = 0
    temp = num

    while temp > 0:
        digit = temp % 10
        rev = rev * 10 + digit
        temp //= 10

    return rev

n = int(input("Enter number: "))

if n == reverse(n):
    print("Palindrome Number")
else:
    print("Not Palindrome Number")