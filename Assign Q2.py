# calculate percentage of  students and average percentage
n = int(input("Enter Number of Students: "))

total_percentage = 0

for i in range(n):
    print("\nStudent", i + 1)

    total = 0

    for j in range(5):
        marks = float(input(f"Enter Marks of Subject {j+1}: "))
        total += marks

    percentage = total / 5
    print("Percentage =", percentage)

    total_percentage += percentage

average = total_percentage / n
print("\nAverage Percentage of Students =", average)