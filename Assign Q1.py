# User id and password (3 times)
userid ="admin"
password ="1234"

for i in range(3):
    userid= input("Enter user id :")
    password=(input("Enter password:"))

    if userid == userid and password ==password:
        print("Login successful")
        break
    else:
        print("Incorrect credentials")

else:
    print("program terminated")