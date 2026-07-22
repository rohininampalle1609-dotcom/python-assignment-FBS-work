# Convert distant given in feet and inches into meter and centimeter.

feet = float(input("Enter distance in feet:"))
inches = float(input("Enter distance in inches:"))

meters = (feet * 0.3048) + (inches * 0.0254)
centimeters = meters * 100

print("Distance in Meters =", meters)
print("Distance in centimeters =",centimeters)
