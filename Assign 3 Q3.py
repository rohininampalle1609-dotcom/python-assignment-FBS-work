# Wap to input angles of triangle and check whether triangle is valid or not

angle1 = int(input("Enter first angle: "))
angle2 = int(input("Enter second angle: "))
angle3 = int(input("Enter third angle: "))

if angle1 + angle2 + angle3 == 180:
    print("Triangle is Valid")
else:
    print("Triangle is Not Valid")