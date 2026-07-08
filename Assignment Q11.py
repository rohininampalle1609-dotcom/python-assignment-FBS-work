# Write a program to enter P.T.R and calculate compound Interest



P = float(input("Enter Principal Amount: "))
R = float(input("Enter Rate of Interest: "))
T = float(input("Enter Time (in years): "))

A = P * (1 + R / 100) ** T
CI = A - P

print("Amount =", A)
print("Compound Interest =", CI)