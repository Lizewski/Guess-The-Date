import json
import random

f = open("database.json", encoding="utf-8")
database = json.load(f)
choice_c = random.choice(list(database.keys()))
listgames = database[choice_c]
tip_c = random.choice(listgames)
f.close()

print(f"""
    Welcome to Guess The Date!
    You have 3 attempts to guess the release date of the game.
      
    The game is: {tip_c}""")

n_choices = 3
while n_choices > 0:
    print(f"You have {n_choices} attempts left.")
    guess = input("Enter your guess (YYYY):\n")
    if guess == choice_c:
        print("Congratulations! The date is correct!")
        break
    else:
        n_choices -= 1
        if n_choices == 0:
            print(f"You lose! Better luck next time. The answer is {choice_c}.")
            break
        print(f"Wrong date! Try again! You have {n_choices} attempts.")
        