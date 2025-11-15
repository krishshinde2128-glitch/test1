import random

print("Welcome to Rock–Paper–Scissors!")

options = ["rock", "paper", "scissors"]

while True:
    user = input("Enter rock, paper, or scissors (or quit to stop): ").lower()

    if user == "quit":
        print("Thanks for playing!")
        break

    if user not in options:
        print("Invalid choice, try again!")
        continue

    computer = random.choice(options)
    print("Computer chose:", computer)

    # Check winner
    if user == computer:
        print("It's a tie!")

    elif (user == "rock" and computer == "scissors") or \
         (user == "paper" and computer == "rock") or \
         (user == "scissors" and computer == "paper"):
        print("You win!")

    else:
        print("You lose!")

    print()  # blank line for readability
