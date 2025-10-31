list1=[1,2,3,4,5] # index: 0,1,2,3,4
print(list1[2]) # accessing element at index 2
list1[2]=True # modifying element at index 2
print(list1[2]) 
list1.pop(0) # removing element at index 0
print(list1) 
list1.append(8) # adding element at the end
print(list1)
list1.insert(2,"krish") # inserting element at index 2
print(list1)
list1.remove(1) # removing element with value 1
print(list1)
for i in reversed(list1): # iterating in reverse order
    print(i)

list2=[5,6,7,8,9]
print(list2[::-1]) # printing reversed list using slicing
print(list2[::2])  # printing list with step 2
print(list2[::3])  # printing list with step 3
print(list2[1:4:1]) # slicing from index 1 to 3
    #(start,stop,step)
print(list2[:-2]) # slicing to exclude last 2 elements
print(list2)