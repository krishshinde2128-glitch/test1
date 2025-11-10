x= int(input("Enter a number: "))
y = 25
def if_even(x):
    if (x % 2 == 0):
        return True
    else:
        raise ValueError("if_even expects an int")
    return False