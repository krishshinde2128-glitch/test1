import random

people = 10

trials = 10000

same_birthday_num = 0

for trial in range(trials):
    birthdays = []

    for _ in range(people):
        day = random.randint(1, 365)
        birthdays.append(day)
    
    if len(birthdays) != len(set(birthdays)):
        same_birthday_num += 1

probability = same_birthday_num / trials

print(f"Out of {trials} simulations, {same_birthday_num} had at least two people sharing a birthday.")
print(f"Estimated Probability: {probability:.4f}")