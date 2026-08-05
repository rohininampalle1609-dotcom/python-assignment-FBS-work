#1
#1 1
#1 2 1
#1 3 3 1

rows = 4

for i in range(rows):
    num = 1
    for j in range(i + 1):
        print(num, end=" ")
        num = num * (i - j) // (j + 1)
    print()