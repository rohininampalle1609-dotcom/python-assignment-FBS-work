# Ticket amount with discount
passengers = int(input("Enter Number of Passengers: "))
ticket = float(input("Enter Ticket Cost: "))

total_amount = 0

for i in range(passengers):
    age = int(input(f"Enter Age of Passenger {i+1}: "))

    if age < 12:
        amount = ticket - (ticket * 30 / 100)

    elif age > 59:
        amount = ticket - (ticket * 50 / 100)

    else:
        amount = ticket

    total_amount += amount

print("Total Ticket Amount =", total_amount)