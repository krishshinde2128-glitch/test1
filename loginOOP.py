# user_input = input("enter you username: ")
# password_input = input("enter you password: ")


# class user:
#     def __init__(self,username,password):
#         self.username = username
#         self.__password = password
    
#     def get_password(self):
#         return self.__password
    


# class Auth(user):

#     def __init__(self,username,password):
#         super().__init__(username, password)
    
#     def login (self, username, password):
#         if self.username == user_input and password == password_input:
#             return  True
#         return False
        
#     def reg():
#         pass

# obj = Auth('krish', 'pass')
# print(obj.login(user_input, password_input))

from abc import ABC , abstractmethod
class Human (ABC):
    @abstractmethod
    def talk():
        print("talking..")

class Man(Human):
    # def talk(self):
    #     print("hmmmmmm")
    def walk(self):
        print("walking")

person = Man()
person.walk()
    