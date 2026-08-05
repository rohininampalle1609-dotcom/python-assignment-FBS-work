#Armstrong number between given range

start = int(input("Enter Starting Number: "))
end = int(input("Enter Ending Number: "))

for num in range(start, end + 1):
    temp = num
    digits = len(str(num))
    total = 0

    while temp > 0:
        rem = temp % 10
        total = total + rem ** digits
        temp = temp // 10

    if total == num:
        print(num)