# WAP  TO FIND WHICH NUMBER ARE DIVISIBLE BY 7 AND MULTIPLE OF IN A GIVEN RANGE.

start = int(input("Enter starting number:"))
end = int(input("Enter ending number:"))

print("Number divisible by 7 and multiples of 5 are:")


for i in range(start, end + 1):
    if i % 7 == 0 and i % 5 == 0:
        print(i)