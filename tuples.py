my_tuples = (1, 2, 3)

# printng single elements
print (my_tuples[0])

# printng useing negative indexing
print (my_tuples[-1])
print (my_tuples[-2])

# Slicing
print (my_tuples[0:2])
print (my_tuples[:2])
print (my_tuples[1:])
print (my_tuples[1:2])

# loop through tuple usinf for loop and while loop
for i in my_tuples:
    print(i)

#looping through tuples using while loop
x = 0
while x < len(my_tuples):
    print(my_tuples[x])
    x  = x + 1

con_tuples = list(my_tuples)
con_tuples[0] = 34
print (con_tuples)