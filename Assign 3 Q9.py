# Input 5 subject marks from user and display grade.(ex 1st class, 2nd class)



sub1 = float(input("Enter marks of Subject 1: "))
sub2 = float(input("Enter marks of Subject 2: "))
sub3 = float(input("Enter marks of Subject 3: "))
sub4 = float(input("Enter marks of Subject 4: "))
sub5 = float(input("Enter marks of Subject 5: "))

total = sub1 + sub2 + sub3 + sub4 + sub5
percentage = total / 5

print("Total Marks =", total)
print("Percentage =", percentage)

if percentage >= 75:
    print("Grade: Distinction")

elif percentage >= 60:
    print("Grade: First Class")

elif percentage >= 50:
    print("Grade: Second Class")

elif percentage >= 35:
    print("Grade: Pass Class")

else:
    print("Grade: Fail")