import json
import random
import os

# ---------- Load or initialize data ----------
def load_json(filename, default):
    if os.path.exists(filename):
        with open(filename, "r") as f:
            return json.load(f)
    else:
        return default

# mapping: which number is assigned to which name
mapping = load_json("mapping.json", {})

# used numbers: which numbers have already been given randomly
used_numbers = load_json("used.json", [])

# ---------- Create mapping only first time ----------
all_names = [
    "Krish", "Aarav", "Vivaan", "Reyansh", "Ishaan",  
    "Vihaan", "Aditya", "Kabir", "Arjun", "Atharv",
    "Sai", "Rohan", "Yash", "Dev", "Karan",
    "Manav", "Harsh", "Shiv", "Aryan", "Rudra", "Om"
]

if not mapping:  # only generate once
    numbers = list(range(21))  # 0–20
    random.shuffle(all_names)
    mapping = {num: name for num, name in zip(numbers, all_names)}
    
    with open("mapping.json", "w") as f:
        json.dump(mapping, f, indent=4)
    print("Mapping generated for the first time!")
else:
    print("Mapping loaded.")

# ---------- Function to get a random unused number ----------
def get_random_unused_number():
    available = [n for n in range(21) if n not in used_numbers]
    if not available:
        return None
    number = random.choice(available)
    used_numbers.append(number)
    with open("used.json", "w") as f:
        json.dump(used_numbers, f, indent=4)
    return number

# ---------- MAIN PROGRAM ----------
while True:
    print("\n1 → Get random unused number")
    print("2 → Enter a number to see its name")
    print("3 → Exit")
    
    choice = input("Choose: ")

    # Option 1: random number
    if choice == "1":
        num = get_random_unused_number()
        if num is None:
            print("⚠ No numbers left!")
        else:
            print(f"Your random number is: {num}")
            print(f"Name → {mapping[str(num)]}")

    # Option 2: lookup name from number
    elif choice == "2":
        num = int(input("Enter number 0–20: "))
        
        if str(num) in mapping:
            print(f"Name for {num} → {mapping[str(num)]}")
        else:
            print("Invalid number.")

    elif choice == "3":
        break
    else:
        print("Invalid choice.")