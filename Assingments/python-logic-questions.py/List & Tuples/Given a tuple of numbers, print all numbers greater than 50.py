my_tuple = (10, 65, 30, 80, 45, 90, 20, 55)
sorted_tuple = sorted(my_tuple)
print("Numbers greater than 50:")
for number in sorted_tuple:
    if number > 50:
        print(number)