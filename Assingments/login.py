class User:
    def __init__(self, name, password):
        self.name = name
        self.password = password


class Authentication:
    def create_user(self):
        name = input("Enter username: ")
        password = input("Enter password: ")   # visible while typing

        user = User(name, password)
        print("User created successfully!\n")

        # When showing password, show stars instead of actual characters
        print("Saved User Details:")
        print("Username:", user.name)
        print("Password:", "*" * len(user.password))

        return user


# -------- RUN PROGRAM --------
auth = Authentication()
auth.create_user()
