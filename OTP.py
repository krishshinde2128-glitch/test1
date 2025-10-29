otp = "123456"
username = "krish"
password = "krish2721"
limit = 3
enter_username = input("Enter your username: ")
enter_password = input("Enter your password: ")
if enter_username == username and enter_password == password:
    print("Login Successful")
elif enter_username == password and enter_password == username:
    print("close but not correct")
else:
    print("Login Failed")

while enter_username == username and enter_password == password and limit <= 3:
    enter_otp = input("Enter your OTP: ")
    if enter_otp == otp:
        print("OTP Verified. Access Granted.")
        break
    else:
        limit -= 1
        if limit == 0:
            print("No attempts left. Access Denied.")
            break
        else:
            print(f"Incorrect OTP. You have {limit} attempts left.")