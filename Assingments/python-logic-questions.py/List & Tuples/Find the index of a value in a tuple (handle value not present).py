my_tuples = (1,2,3,4)

user_input = int(input("enter a value to find index"))
if user_input in list(my_tuples):
    for x in my_tuples:
        print(x.index())
else:
    print("input number doesnt exist ")
    