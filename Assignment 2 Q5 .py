# Write to calculate  selling price of book based on cost price  abd discount.

cost_price = float(input("Enter the cost price of the book:"))
discount = float(input("Enter the discount percentege:"))

discount_amount = (cost_price * discount) / 100
selling_price = cost_price - discount_amount

print("Discount Amount = ", discount_amount)
print("Selling price =",selling_price)
