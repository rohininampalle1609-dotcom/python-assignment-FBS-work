# Write a program to convert days into years and weeks

day = int (input("Enter days"))

years = day // 365
#print(years)

day = day % 356
# print(days)

week = day // 7
# print(days)

day = day % 7
# print (days)

print ("f" "years:{years},weeks:{weeks},days{days}")