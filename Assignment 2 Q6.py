# Write program calculate salary of employee based on basic ,da=10% of basic,ta = 12% of basic, hra=15% of basic

basic = float(input(" Enter basic salary:"))

da = ( basic * 10 ) / 100
ta = ( basic * 12 ) / 100
hra = ( basic * 15 ) / 100

gross_saalry= basic + da + ta + hra

print(" Basic salary=", basic)
print("DA =",da)
print("TA =", ta)
print("HRA =", hra)
print("Gross saalry =", gross_saalry)
