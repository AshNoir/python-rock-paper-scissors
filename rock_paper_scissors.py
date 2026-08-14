# Import random module to generate the computer's random choice
import random


# Main game function
def r_p_s():

    # Game title and menu
    s = """
================================
      ROCK PAPER SCISSORS
================================

1. Rock
2. Paper
3. Scissors
4. Exit
"""

    print(s)

    # Available choices for the computer
    choices = ["Rock", "Paper", "Scissors"]

    # Overall score counters
    ysc = 0
    csc = 0
    dsc = 0

    # Main game loop
    while True:

        # Ask the player to select a move
        ch = int(input("Enter: "))

        # Dictionary used to display the result of the current round
        optn = {
            "You": 0,
            "Computer": 0,
            "Draws": 0
        }

        # Computer randomly selects Rock, Paper or Scissors
        pick = random.choice(choices)

        # ---------------- ROCK ----------------

        if ch == 1:

            print("You chose Rock")

            # Both choose Rock
            if pick == "Rock":

                print("Computer chose Rock")

                optn["Draws"] += 1
                dsc += 1

            # Computer chooses Paper
            elif pick == "Paper":

                print("Computer chose Paper")

                optn["Computer"] += 1
                csc += 1

            # Computer chooses Scissors
            else:

                print("Computer chose Scissors")

                optn["You"] += 1
                ysc += 1


            # Display current round result
            print("Score")
            print("----------------")

            for k, v in optn.items():
                print(f"{k}: {v}")

            print("----------------")


        # ---------------- PAPER ----------------

        elif ch == 2:

            print("You chose Paper")

            # Both choose Paper
            if pick == "Paper":

                print("Computer chose Paper")

                optn["Draws"] += 1
                dsc += 1

            # Paper beats Rock
            elif pick == "Rock":

                print("Computer chose Rock")

                optn["You"] += 1
                ysc += 1

            # Scissors beats Paper
            else:

                print("Computer chose Scissors")

                optn["Computer"] += 1
                csc += 1


            # Display current round result
            print("Score")
            print("----------------")

            for k, v in optn.items():
                print(f"{k}: {v}")

            print("----------------")


        # ---------------- SCISSORS ----------------

        elif ch == 3:

            print("You chose Scissors")

            # Both choose Scissors
            if pick == "Scissors":

                print("Computer chose Scissors")

                optn["Draws"] += 1
                dsc += 1

            # Rock beats Scissors
            elif pick == "Rock":

                print("Computer chose Rock")

                optn["Computer"] += 1
                csc += 1

            # Scissors beats Paper
            else:

                print("Computer chose Paper")

                optn["You"] += 1
                ysc += 1


            # Display current round result
            print("Score")
            print("----------------")

            for k, v in optn.items():
                print(f"{k}: {v}")

            print("----------------")


        # ---------------- EXIT ----------------

        elif ch == 4:

            # Final score screen
            scr = """
================================
         FINAL SCORE
================================
"""

            print(scr)

            # Display overall scores
            scre = f"""
You      : {ysc}
Computer : {csc}
Draws    : {dsc}
"""

            print(scre)

            # Decide the overall winner
            if csc > ysc:

                print("COMPUTER WINS THE MATCH :(")

            elif ysc == csc:

                print("It's A Draw!")

            else:

                print("🏆 YOU WIN THE MATCH!")

            # End the game
            break


        # ---------------- INVALID INPUT ----------------

        else:

            print("Invalid Output :(")


# Start the game
r_p_s()
