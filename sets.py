my_set = {8, 2, 3, True, 4} # Creating a set with initial elements
#my_set[0]

for x in my_set: 
    print(x)

my_set.add("Q") # Adding "Q" to the set (adds it anywhere)
print(my_set)
for x in my_set:
    print(x)

my_set.remove(3) # Removing 3 from the set
print(my_set)
for x in my_set:
    print(x)

my_set.pop() # Removing an arbitrary element from the set
print(my_set)
for x in my_set:
    print(x)

my_set.discard(10) # Trying to remove 10 which is not in the set (no error)
print(my_set)
for x in my_set:
    print(x)

my_set.clear() # Clearing all elements from the set
print(my_set)
for x in my_set:
    print(x)