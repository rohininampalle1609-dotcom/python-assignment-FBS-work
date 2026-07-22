
# Program to calculate total ticket amount for 5 people

ticket = float(input("Enter Ticket Amount per Person: "))

total = 0

for i in range(1, 6):
    age = int(input("Enter age of Person " + str(i) + ": "))

    if age < 12:
        amount = ticket - (ticket * 30 / 100)

    elif age > 59:
        amount = ticket - (ticket * 50 / 100)

    else:
        amount = ticket

    total = total + amount

print("Total Ticket Amount =", total)