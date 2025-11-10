x = int(input("Enter a number: "))
try:
    print("You entered:", x)
except Exception as e:
    print("default", e)
else:
    print("inside else")
finally:
    print("inside finally")