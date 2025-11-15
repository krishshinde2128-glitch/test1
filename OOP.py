class student:
    

    def __init__(self,roll_number):
        self.roll_number = roll_number

    def learn(self):
        return "Learning..."

james = student(157)
print(james.roll_number)
print(james.learn())
# krish = student(158)
# trisha = student(159)
# paarth = student(160)

class teacher:
    pass

prasad = teacher()
prasad.skill = ["python", "c++", "java"]
print(prasad.skill)

#gatik = teacher()
#gatik.skill = print(gatik.skill)

class person:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def print_fullname(self):
        return self.fname + " " + self.lname

class User(person):
    def __init__(self,fname,lname):
        super().__init__(fname, lname)


    def print_fullname(self):
        return self.fname + " " + self.lname
    
    def set_username(self):
        return self.fname
user_one = User("john", "krish")
print(user_one.fname)
print(user_one.lname)
print(user_one.print_fullname())