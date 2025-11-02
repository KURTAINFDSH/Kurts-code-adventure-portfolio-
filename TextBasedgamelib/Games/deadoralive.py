import random as rd
import os
import sys

sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), "Games"))

import gamelibrary

def main():
  print("-------- |dead or alive| --------")
  print("choose 1 to 9 your life depends on the number you pick")
  player_choice = int(input("choice: "))
  
  danger_num = rd.randint(1, 9)
  danger_num2 = rd.randint(1, 9)
  danger_num3 = rd.randint(1, 9)
  danger_num4 = rd.randint(1, 9)
  
  if player_choice == danger_num and player_choice == danger_num4 and player_choice == danger_num2 and player_choice == danger_num3:
    print("you died")
    
  else:
    print("you survive")
    print(danger_num, danger_num3, danger_num4, danger_num2)
    print("[1] play again or [2]exit")
    
    choice = input("choice: ")
    if choice == "1":
      main()
      
    else:
      gamelibrary.main()