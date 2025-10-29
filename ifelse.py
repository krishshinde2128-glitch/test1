username = "krish"
password = "krish2721"
if username == "krish" and password == "krish2721":
    print("Login Successful")

a= id(username)
b= id(password)
if username == a and password == b:
    print("Login done")

enter_username = input("Enter your username: ")
enter_password = input("Enter your password: ")
if enter_username == username and enter_password == password:
    print("Login Successful")
elif enter_username == password and enter_password == username:
    print("close but not correct")
else:
    print("Login Failed")   

