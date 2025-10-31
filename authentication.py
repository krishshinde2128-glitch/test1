username = "krish"
password = "krish2721"

enter_username = input("Enter your new username: ")
enter_password = input("Enter your new password: ")


if enter_username == username and enter_password == password:
    print("Login Successful")
elif enter_username == password and enter_password == username:
    print("close but not it try again")
else:
    print("Login Failed")