x=input("Enter a string: ")
y=""
for char in x:
    if char not in y:
        y+=char

print("String without duplication", y)
