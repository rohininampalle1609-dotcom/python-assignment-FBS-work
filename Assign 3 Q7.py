# Wap to prompt user tp enter userid and password . After verifying userid anf password display a 4 digit random number and ask user to enter the  same . If user enter the same number then show him success msg otherwise faild.(something like captcha)

# Program for User ID, Password and CAPTCHA Verification

import random

userid = input("Enter User ID: ")
password = input("Enter Password: ")

if userid == "admin" and password == "1234":

    captcha = random.randint(1000, 9999)

    print("Captcha:", captcha)

    user_captcha = int(input("Enter the Captcha: "))

    if user_captcha == captcha:
        print("Login Successful")
    else:
        print("Captcha Verification Failed")

else:
    print("Invalid User ID or Password")