import random

print("🏏 Welcome to FULL Odd–Even Cricket Game!")

# --- TOSS ---

print("\n--- TOSS TIME ---")

# Validate odd/even input
while True:
    choice = input("Choose Odd or Even: ").lower()
    if choice in ["odd", "even"]:
        break
    else:
        print("Invalid input! Type only 'Odd' or 'Even'. Try again.\n")

comp_num = random.randint(1, 6)

while True:
    user_num = int(input("Enter a number between 1 and 6: "))
    if user_num <= 6 and user_num >= 1:
        break
    else:
        print ("Invalid input! Type only from 1 to 6. Try again.\n")

print("Computer chose:", comp_num)

total = user_num + comp_num
toss_result = "even" if total % 2 == 0 else "odd"

# Decide toss winner
if choice == toss_result:
    print("\n🎉 You won the toss!")

    # VALIDATE bat/bowl input
    while True:
        user_bats = input("Do you want to bat or bowl first? ").lower()
        if user_bats in ["bat", "bowl"]:
            break
        else:
            print("Invalid input! Type only 'bat' or 'bowl'. Try again.\n")

else:
    print("\n💻 Computer won the toss!")
    user_bats = random.choice(["bat", "bowl"])
    print("Computer chooses to", user_bats)

# ================================
#           FIRST INNINGS
# ================================
def get_number(prompt):
    while True:
        try:
            num = int(input(prompt))
            if 1 <= num <= 6:
                return num
            else:
                print("Invalid input! Enter a number between 1 and 6.\n")
        except ValueError:
            print("Invalid input! Enter digits only (1–6).\n")


print("\n--- FIRST INNINGS START ---")
score1 = 0

if user_bats == "bat":     # User bats first
    print("\nYou are BATTING first!")
    while True:
        user_play = get_number("Enter your run (1–6): ")
        comp_play = random.randint(1, 6)
        print("Computer bowled:", comp_play)

        if user_play == comp_play:
            print("\n❌ OUT!")
            print("Your 1st innings score:", score1)
            break
        else:
            score1 += user_play
            print("Runs:", score1)

else:                       # Computer bats first
    print("\nComputer is BATTING first!")
    while True:
        user_play = get_number("Enter your bowl (1–6): ")
        comp_play = random.randint(1, 6)
        print("Computer played:", comp_play)

        if user_play == comp_play:
            print("\n🎯 You GOT the computer OUT!")
            print("Computer's 1st innings score:", score1)
            break
        else:
            score1 += comp_play
            print("Computer score:", score1)

# ================================
#           SECOND INNINGS
# ================================


print("\n--- SECOND INNINGS START ---")
print("Target:", score1 + 1)
score2 = 0

if user_bats == "bowl":   # Now user bowls
    print("\nYou are BATTING now!")
    while True:
        user_play = get_number("Enter your run (1–6): ")
        comp_play = random.randint(1, 6)
        print("Computer bowled:", comp_play)

        if user_play == comp_play:
            print("\n❌ OUT!")
            print("Your final score:", score2)
            break
        else:
            score2 += user_play
            print("Runs:", score2)

            if score2 > score1:
                print("\n🎉 YOU CHASED THE TARGET!")
                break
else:                    # Computer bats second
    print("\nComputer is BATTING now!")
    while True:
        user_play = get_number("Enter your bowl (1–6): ")
        comp_play = random.randint(1, 6)
        print("Computer played:", comp_play)

        if user_play == comp_play:
            print("\n🎯 You got the computer OUT!")
            print("Computer's final score:", score2)
            break
        else:
            score2 += comp_play
            print("Computer score:", score2)

            if score2 > score1:
                print("\n💻 COMPUTER CHASED THE TARGET!")
                break

# ================================
#             RESULT
# ================================

print("\n--- MATCH RESULT ---")

if score2 > score1:
    if user_bats == "bat":
        print("💻 Computer wins!")
    else:
        print("🎉 You win!")

elif score1 > score2:
    if user_bats == "bat":
        print("🎉 You win!")
    else:
        print("💻 Computer wins!")

else:
    print("🤝 Match TIED!")