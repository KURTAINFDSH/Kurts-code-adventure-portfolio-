import sys
import os
import json

sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), "Games"))

path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data")

playerpath = os.path.join(path, "player.json")

with open(playerpath, "r") as file:
  loaded = json.load(file)

import guess
import rpsgame
import mathgame
import Numfight
import decrypt
import deadoralive

def clear_screen():
	os.system('clear')

def main():
    clear_screen()
    
    print("------------| Game Library |-----------")
    print("1.| Guessing Game  |6. dead or alive | ")
    print("2.| Jack and po    |7.               | ")
    print("3.| Math Quiz Game |8.               | ")
    print("4.| Number Fight   |9.               | ")
    print("5.| Decrypt a pass |10.              | ")
    print("---------------|Profile|---------------")
    
    player_name = loaded["name"]
    player_win = loaded["wins"]
    player_score = loaded["scores"]
    
    print(f"Name: {player_name}")
    print(f"Total wins: {player_win}")
    print(f"Total scores: {player_score}")
    
    print("----------------------------")
    
    choose = input("Choose a game: ")

    if choose == "1":
        guess.guess_game()
    elif choose == "2":
        rpsgame.rpsg()
    elif choose == "3":
        mathgame.math_quiz()
    elif choose == "4":
    	Numfight.main()
    elif choose == "5":
      decrypt.main()
    elif choose == "6":
      deadoralive.main()
    	
    else:
        print("Invalid choice!")

if __name__ == "__main__":
    main()