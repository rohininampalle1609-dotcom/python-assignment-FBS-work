# COMPOUND INTEREST
p= float(input("Principal:"))
r = float(input("Rate:"))
t = float(input("Time:"))

amount = 'p'* (1 + r / 100)** t
ci = amount - p

print("Compound Interest =",ci)