import random
import sys
import os
import json

sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), "Games"))

path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data")

player_path = os.path.join(path, "player.json")

with open(player_path, "r") as file:
    loaded = json.load(file)

wins = 0
g2 = ["rock", "paper", "scissors"]
max_round = 3

def clear_screen():
    os.system('clear')

def rpsg():
    global wins
    rounds = 0
    clear_screen()
    
    print("| Rock, Paper, Scissors Game |")
    
    while rounds < max_round:
        bot_pick = random.choice(g2)
        your_choice = input("| Your choice |: ").lower()
        
        if your_choice == "exit":
            import gamelibrary
            gamelibrary.main()
            return
        
        print(f"| Bot choosed |: {bot_pick}")
        rounds += 1
        
        if your_choice == bot_pick:
            print(" Tie! |   |  Bot |: hmmmm ")
        
        elif (your_choice == "rock" and bot_pick == "scissors") or \
             (your_choice == "paper" and bot_pick == "rock") or \
             (your_choice == "scissors" and bot_pick == "paper"):
            
            wins += 1
            loaded["wins"] = loaded.get("wins", 0) + 1
            
            print(f"You Won! | Wins this game: {wins} |")
            print("| Bot |: you just got lucky!")
            
            with open(player_path, "w") as file:
                json.dump(loaded, file, indent=4)
        
        else:
            print("You lose! | Bot |: dumb bastard")
    
    print(f"Game over! Total wins this session: {wins}")
    
    play_again = input("|1. Play again | 2. Quit |: ")
    if play_again == "1":
        rpsg()
    else:
        import gamelibrary
        gamelibrary.main()
 