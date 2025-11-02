import random as rd
import sys
import os

sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), "Games"))

import gamelibrary

def main():
    max_guesses = 10
    score = 0

    while True:
        guesses = 0
        p = [rd.randint(1, 9) for _ in range(4)]
        p2 = ''.join(map(str, p))
        
        print(" | Decrypt A Password | ")
        hint = ["_"] * 4
        
        while guesses < max_guesses:
            player = input("Hacker: ")
            
            if len(player) != 1 or not player.isdigit() or player == "0":
                print("Enter exactly 1 digit (1-9).")
                continue
            
            guesses += 1
            
            for i in range(4):
                if player == p2[i]:
                    hint[i] = player
            
            print(f"Hint | {' '.join(hint)} | ")
            print(f"Guesses left: {max_guesses - guesses}")
            
            if ''.join(hint) == p2:
                print("You successfully decrypted the password!")
                score += 1
                break
        else:
            print(f"Failed to decrypt | {p2} |")
        
        play_again = input("|1. Play again | 2. Quit | ")
        if play_again == '1':
            continue
        elif play_again == "2":
            gamelibrary.main()
            break