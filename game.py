import json
import random
import sys
from custom import printcenter

def fchoice():
    with open("database.json", encoding="utf-8") as f:
        database = json.load(f)
    choice_c = random.choice(list(database.keys()))
    listgames = database[choice_c]
    tip_c = random.choice(listgames)
    printcenter(f"""
        Welcome to Guess The Date!
        You have 3 attempts to guess the release date of the game.
        
        The game is: {tip_c}\n""")
    return choice_c


def start(choice_c):
    while True:
        n_choices = 3
        while n_choices > 0:
            guess = input("Enter your guess (YYYY):\n")
            if guess == choice_c:
                printcenter("\nCongratulations! The date is correct!\n")
                break
            else:
                n_choices -= 1
                if n_choices == 0:
                    printcenter(f"You lose! Better luck next time. The answer is {choice_c}.\n")
                    break
                printcenter(f"\nWrong date! Try again!\nThe chosen game was released {'after' if int(guess) < int(choice_c) else 'before'} {guess}.\nYou have {n_choices} attempts left.\n")
        break


def playagain():
    while True:
        again = input("Do you want to play again? (Yes / No)\n").strip().upper()[0]
        if again == "Y":
            return True
        elif again == "N":
            printcenter("Game Over!")
            return False
        else: 
            printcenter("Incorrect! Let's try again...")
        

def main():
    while True:
        choice_c = fchoice()
        start(choice_c)
        if playagain() == False:
            break


if __name__ == "__main__":
    main()
    sys.exit()