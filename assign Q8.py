# N + N2+ N3 + N4 +.....+NN

N = int(input("Enter N: "))

sum = 0

for i in range(1, N + 1):
    sum = sum + N ** i

print("Sum =", sum)