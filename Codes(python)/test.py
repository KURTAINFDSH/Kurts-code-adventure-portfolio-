import random
import os
import sys

sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), "Games"))

import gamelibrary

def clear_screen():
	os.system('clear')

def lbot():
    return random.randint(1, 9)

def locks():
    return random.randint(1, 9), random.randint(1, 9), random.randint(1, 9), random.randint(1, 9)

def main():
    clear_screen()
    
    print("----------- | Number Fight | ---------")
    
    while True:
        phealth = 5
        bhealth = 5
        lock1, lock2, lock3, lock4 = locks()

        while phealth > 0 and bhealth > 0:
            player = int(input("Player: "))
            bot = lbot()
            print(f"Bot chose: {bot}")
            
            if player in (lock1, lock2, lock3, lock4):
                print("You hit a lock!")
                phealth -= 1
            
            if bot in (lock1, lock2, lock3, lock4):
                print("Bot hit a lock!")
                bhealth -= 1
            
            if player > bot:
                print("You win this round!")
                bhealth -= 1
            elif player < bot:
                print("You lose this round!")
                phealth -= 1
            else:
                print("Tie!")
            
            print(f"Player: {phealth} | Bot: {bhealth}")
        
        if phealth <= 0:
            print("You lose")
        elif bhealth <= 0:
            print("You won")
        
        m = input("exit or  retry: ")
        if m.lower() == "exit":
            gamelibrary.main()
            break 
            
        else:
        	main()
        	
main()        	