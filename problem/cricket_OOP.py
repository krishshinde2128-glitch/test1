import random

# -------------------------------------------
# VALIDATED INPUT (1–6 ONLY)
# -------------------------------------------
def get_number(prompt):
    while True:
        try:
            num = int(input(prompt))
            if 1 <= num <= 6:
                return num
            print("Invalid! Enter a number between 1–6.\n")
        except ValueError:
            print("Invalid! Enter digits only (1–6).\n")


# -------------------------------------------
# PLAYER CLASS
# -------------------------------------------
class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0

    def play_move(self, is_user=False):
        if is_user:
            return get_number("Enter your number (1–6): ")
        return random.randint(1, 6)

    def reset_score(self):
        self.score = 0


# -------------------------------------------
# TOSS CLASS
# -------------------------------------------
class Toss:
    def do_toss(self):
        while True:
            choice = input("Choose Odd or Even: ").lower()
            if choice in ["odd", "even"]:
                break
            print("Invalid! Enter 'odd' or 'even'.\n")

        user_num = get_number("Enter a number between 1–6: ")
        comp_num = random.randint(1, 6)

        print("Computer chose:", comp_num)

        total = user_num + comp_num
        result = "even" if total % 2 == 0 else "odd"

        if choice == result:
            print("\n🎉 You won the toss!")
            return "user"
        else:
            print("\n💻 Computer won the toss!")
            return "computer"


# -------------------------------------------
# INNINGS CLASS
# -------------------------------------------
class Innings:
    def start(self, batter, bowler, user_is_batting):
        batter.reset_score()

        print(f"\n{batter.name} is BATTING!")
        print("---------------------------")

        while True:
            if user_is_batting:
                play1 = batter.play_move(is_user=True)
                play2 = bowler.play_move()
            else:
                play1 = batter.play_move()
                play2 = bowler.play_move(is_user=True)

            print(f"{batter.name} played:", play1)
            print(f"{bowler.name} played:", play2)

            if play1 == play2:
                print(f"\n❌ {batter.name} is OUT!")
                print(f"{batter.name}'s final score:", batter.score)
                break
            else:
                batter.score += play1
                print(f"{batter.name} score:", batter.score)

        return batter.score


# -------------------------------------------
# CRICKET GAME CLASS
# -------------------------------------------
class CricketGame:
    def __init__(self):
        self.user = Player("User")
        self.comp = Player("Computer")
        self.toss = Toss()

    def start(self):
        print("\n🏏 Welcome to OOP Odd–Even Cricket!\n")

        # --------- TOSS ---------
        winner = self.toss.do_toss()

        if winner == "user":
            while True:
                choice = input("Do you want to bat or bowl first? ").lower()
                if choice in ["bat", "bowl"]:
                    break
                print("Invalid input! Enter 'bat' or 'bowl'.\n")
            user_bats_first = (choice == "bat")
        else:
            comp_choice = random.choice(["bat", "bowl"])
            print("Computer chooses to", comp_choice)
            user_bats_first = (comp_choice == "bowl")

        # --------- FIRST INNINGS ---------
        innings = Innings()
        print("\n--- FIRST INNINGS START ---")

        if user_bats_first:
            score1 = innings.start(self.user, self.comp, user_is_batting=True)
            first_batter = "user"
        else:
            score1 = innings.start(self.comp, self.user, user_is_batting=False)
            first_batter = "computer"

        target = score1 + 1
        print(f"\n🔥 Target for second innings: {target}")

        # --------- SECOND INNINGS ---------
        print("\n--- SECOND INNINGS START ---")

        if first_batter == "user":
            score2 = innings.start(self.comp, self.user, user_is_batting=False)
        else:
            score2 = innings.start(self.user, self.comp, user_is_batting=True)

        # --------- RESULT ---------
        print("\n🏁 --- MATCH RESULT ---")

        if first_batter == "user":
            if score2 > score1:
                print("💻 Computer WINS the match!")
            elif score1 > score2:
                print("🎉 YOU WIN the match!")
            else:
                print("🤝 Match TIED!")
        else:
            if score2 > score1:
                print("🎉 YOU WIN the match!")
            elif score1 > score2:
                print("💻 Computer WINS the match!")
            else:
                print("🤝 Match TIED!")


# -------------------------------------------
# RUN GAME
# -------------------------------------------
game = CricketGame()
game.start()
