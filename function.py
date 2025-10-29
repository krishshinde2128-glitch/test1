x = 10

def sum_with_void(x):
    sayhello()
    print(x+1)

def sayhello():
    print("Hello!!")


def sum_with_return(x):
	return(x+1)
y = 10

sum_with_void(y)
print(sum_with_return(20))