import random

number_to_guess = random.randint(100, 999)
print(number_to_guess)
attempts = 0
max_attempts = 10
while attempts < max_attempts:
    x = int(input("guess a 3 digit number: "))
    attempts += 1
    if len(str(x)) != 3:
        print(f"Please enter a 3 digit number , you entered an {len(str(x))} digit number,you have ", max_attempts - attempts, "attempts left.")
    else:
        if attempts == max_attempts:
            print(f"Sorry no more attempts left. The correct number was {number_to_guess}.")
            break
        if x == number_to_guess:
            print("You guessed the correct number.")
            break
        elif x < number_to_guess:
            print("Your guess is too low. you have", max_attempts - attempts, "attempts left.")
        elif x > number_to_guess:
            print("Your guess is too high. you have", max_attempts - attempts, "attempts left.")

        target = str(number_to_guess)
        guess = str(x)
        found_any = False
        for i in range(3):
            if guess[i] == target[i]:
                print("Digit", guess[i], "is correct and in the correct position.")
                found_any = True
            elif guess[i] in target:
                print("Digit", guess[i], "is correct but in the wrong position.")
                found_any = True
        if not found_any:
            print("None of the digits you guessed are in the number.")