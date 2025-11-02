import random
import os
import sys

sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), "Games"))

import gamelibrary

wins = 0
bchosen = []
pchosen = []
available = list(range(1, 10))

def clear_screen():
    os.system('clear')

def lbot():
    bot = random.randint(1, 9)
    bchosen.append(bot)
    return bot

def locks():
    return random.randint(1, 9), random.randint(1, 9)

def main():
    global wins, bchosen, pchosen, available
    clear_screen()
    
    print("----------- | Number Fight | ---------")
    
    while True:
        phealth = 5
        bhealth = 5
        lock1, lock2 = locks()

        while phealth > 0 and bhealth > 0:
            try:
                n = int(input("Player: "))
            except ValueError:
                print("Enter a valid number 1-9")
                continue

            if n not in available:
                print("you picked it already! pick again")
                continue

            pchosen.append(n)
            available.remove(n)

            bot = lbot()
            print(f"Bot chose: {bot}")

            if n in (lock1, lock2):
                print("You hit a lock!")
                phealth -= 1
                print(f"Player: {phealth} | Bot: {bhealth}")
                continue

            if bot in (lock1, lock2):
                print("Bot hit a lock!")
                bhealth -= 1
                print(f"Player: {phealth} | Bot: {bhealth}")
                continue

            if n > bot:
                print("You win this round!")
                bhealth -= 1
            elif n < bot:
                print("You lose this round!")
                phealth -= 1
            else:
                print("Tie!")

            print(f"Player: {phealth} | Bot: {bhealth}")

        if phealth <= 0:
            print("You lose")
        elif bhealth <= 0:
            print("You won")
            wins += 1
            print(f"wins : {wins}")

        m = input("exit or  retry: ")
        if m.lower() == "exit":
            gamelibrary.main()
            break 
        else:
            main()
            