# sum of geometric series(common retio=2)
#1 + 2 +  4 + 8 +......


n = int(input("Enter Number of Terms: "))

sum = 0
term = 1

for i in range(n):
    sum = sum + term
    term = term * 2

print("Sum =", sum)