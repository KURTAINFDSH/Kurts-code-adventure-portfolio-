import random
import os
import sys
import json

sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), "Games"))

path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data")

player_path = os.path.join(path, "player.json")

with open(player_path, "r") as file:
  loaded = json.load(file)
  
num = [1, 2, 3, 4, 5, 6, 7, 8, 9]
score = 0

def clear_screen():
    os.system('clear')

def guess_game():
    global score
    clear_screen() 
    
    print("--------- | Guessing Game | ---------")
    print("| Welcome to Guess Game |")

    pick = random.choice(num)
    guess = None

    while guess != pick:
        try:
            guess = int(input("Your guess: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if guess < pick:
            print("Higher!")
        elif guess > pick:
            print("Lower!")

    # Correct guess
    score += 1
    loaded["scores"] = loaded["scores"] + score
    print(f"You guessed it correctly!\nScore: {score}")

    while True:
        choice = input("[retry] or [quit]: ").lower()
        if choice == "quit":
          with open(player_path, "w") as file:
            json.dump(loaded, file, indent=4)
            
            import gamelibrary 
            gamelibrary.main()
            break
          
        elif choice == "retry":
            guess_game()
            break
        else:
            print("Invalid choice. Type 'retry' or 'quit'.")

    while guess != pick:
        try:
            guess = int(input("Your guess: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if guess < pick:
            print("Higher!")
        elif guess > pick:
            print("Lower!")

    # Correct guess
    score += 1
    loaded["scores"] = loaded["scores"] + score
    print(f"You guessed it correctly!\nScore: {score}")

    while True:
        choice = input("[retry] or [quit]: ").lower()
        if choice == "quit":
          with open(player_path, "w") as file:
            json.dump(loaded, file, indent=4)
            
            import gamelibrary 
            gamelibrary.main()
            break
          
        elif choice == "retry":
            guess_game()
            break
        else:
            print("Invalid choice. Type 'retry' or 'quit'.")