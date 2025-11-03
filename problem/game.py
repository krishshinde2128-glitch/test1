# ...existing code...
import random
from collections import Counter

def play():
    number_to_guess = random.randint(100, 999)
    attempts = 0
    max_attempts = 10

    while attempts < max_attempts:
        s = input("Guess a 3-digit number: ").strip()
        if not s.isdigit() or len(s) != 3:
            print(f"Please enter a 3-digit number; you entered {len(s)} digit(s).")
            continue

        attempts += 1
        guess = s
        target = str(number_to_guess)

        if guess == target:
            print(f"You guessed the correct number in {attempts} attempt(s).")
            return

        # Determine exact matches and wrong-position matches (accounting for duplicates)
        exact_indices = []
        target_counts = Counter(target)

        # First pass: exact position matches
        for i in range(3):
            if guess[i] == target[i]:
                exact_indices.append(i)
                target_counts[guess[i]] -= 1

        # Second pass: same digit but different position
        wrong_position_indices = []
        for i in range(3):
            if i in exact_indices:
                continue
            if target_counts[guess[i]] > 0:
                wrong_position_indices.append(i)
                target_counts[guess[i]] -= 1

        # Print hints
        for i in exact_indices:
            print(f"Digit {guess[i]} is correct and in the correct position (position {i+1}).")
        for i in wrong_position_indices:
            print(f"Digit {guess[i]} is in the number but in a different position.")
        if not exact_indices and not wrong_position_indices:
            print("No digits are correct.")

        if attempts < max_attempts:
            print(f"You have {max_attempts - attempts} attempt(s) left.")
        else:
            print(f"Sorry, no more attempts left. The correct number was {number_to_guess}.")
            return

if __name__ == "__main__":
    play()