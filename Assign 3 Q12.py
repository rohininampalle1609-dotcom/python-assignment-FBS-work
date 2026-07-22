# Program to check whether a 3-digit number is palindrome or not

num = int(input("Enter a three-digit number: "))

digit1 = num // 100
digit2 = (num // 10) % 10
digit3 = num % 10

reverse = (digit3 * 100) + (digit2 * 10) + digit1

if num == reverse:
    print("Palindrome Number")
else:
    print("Not a Palindrome Number")