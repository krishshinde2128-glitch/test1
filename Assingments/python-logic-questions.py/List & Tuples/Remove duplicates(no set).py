def remove_duplicate(input_list):
    return list(dict.fromkeys(input_list))

my_list = [1,2,3,4,5,6,6]
x = remove_duplicate(my_list)
print(x)