import random
import os
import time

DICE_ART = {
    1: ("┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘"),
    2: ("┌─────────┐",
        "│  ●      │",
        "│         │",
        "│      ●  │",
        "└─────────┘"),
    3: ("┌─────────┐",
        "│  ●      │",
        "│    ●    │",
        "│      ●  │",
        "└─────────┘"),
    4: ("┌─────────┐",
        "│  ●   ●  │",
        "│         │",
        "│  ●   ●  │",
        "└─────────┘"),
    5: ("┌─────────┐",
        "│  ●   ●  │",
        "│    ●    │",
        "│  ●   ●  │",
        "└─────────┘"),
    6: ("┌─────────┐",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "└─────────┘")
}

player_money = 500
bot1_money = 500
bot2_money = 500
bot3_money = 500
total_pot = 0

def gamble():
  os.system('clear')
  global player_money, bot1_money, bot2_money, bot3_money, game_bid
  
  print("___________________Roll A Dice___________________")
  print(f"Balance : {player_money}")
  while True:
    
    try:
      player = int(input("\nchoose a number |  "))
    except ValueError:
      print("\nIt must be a valid number\n")
      continue
    
    if player > 6:
      print("--------------------\n")
      print("choose only in 1 to 6\n")
      print("--------------------")
      continue
    
    try:
      player_bid = int(input("Your bid | "))
    except ValueError:
      print("\nIt must be a valid number\n")
      continue
    
    if player_bid > player_money:
      print("\nYou dont have enough balance:")
      print(f"currend balance: {player_money}\n")
      continue
    
    bot1 = random.choice([n for n in range(1, 6)if n != player]) if bot1_money >= 100 else None
      
    bot2 = random.choice([n for n in range(1, 6) if n not in (player, bot1)]) if bot2_money >= 100 else None
    
    bot3 = random.choice([n for n in range(1, 6) if n not in (player, bot1, bot2)]) if bot3_money >= 100 else None
    
    bot3_bid = random.randint(1, min(200, bot3_money)) if bot3_money >= 100 else 0
    bot2_bid = random.randint(1, min(200, bot2_money)) if bot2_money >= 100 else 0
    bot1_bid = random.randint(1, min(200, bot1_money)) if bot1_money >= 100 else 0
    
    bot3_money -= bot3_bid
    bot2_money -= bot2_bid
    player_money -= player_bid
    bot1_money -= bot1_bid

    total_pot = player_bid + bot1_bid + bot2_bid + bot3_bid
  
    print("________________________________\n")
    print(f"bot1 chosses {bot1} and bidded {bot1_bid}")
    print(f"bot3 chosses {bot3} and bidded {bot3_bid}")
    print(f"bot2 chosses {bot2} and bidded {bot2_bid}")
    print(f"Total pot is {total_pot}")
    print("_______________________________")
    
    numbers = list(range(1, 7))
    a = random.choice(numbers)
    
    print("______________Rolling____________")
    
    for dice in range(1, a + 1):
      print("\n" .join(DICE_ART[dice]))
      time.sleep(0.99)
      
    print("_______________dice_______________\n")
    print(f"it landed in {a}\n")
    print("___________Result_____________")
  
    if player == a and player_bid:
      player_money += bot1_bid + bot2_bid + bot3_bid
      print("Player won")
      print(f"Balance : {player_money}")
      print("___________________________")
      
    else:
      print("Player1 loses")
      print(f"Balance : {player_money}")
      print("___________________________")
      
        
    if bot1 == a and bot1_bid:
      bot1_money += player_bid + bot2_bid + bot3_bid
      print("Bot1 Won")
      print(f"Balance {bot1_money}")
      print("___________________________")
      
    else:
      print("bot1 loses")
      print(f"Balance: {bot1_money}")
      print("___________________________")
      
      
    if bot2 ==  a and bot2_bid:
      bot2_money += bot1_bid + player_bid + bot3_bid
      print("Bot2 Won")
      print(f"Balance {bot2_money}")
      print("___________________________")
      
    else:
      print("Bot2 loses")
      print(f"Balance: {bot2_money}")
      print("___________________________")
      
      
    if bot3 == a and bot3_bid:
      bot3_money += player_bid + bot1_bid + bot2_bid
      print("Bot3 Won")
      print(f"Balance {bot3_money}")
      print("___________________________\n")
      
    else:
      print("bot3 loses")
      print(f"balance: {bot3_money}")
      print("___________________________")
      
    if player != a and bot1 != a and bot2 != a and bot3 != a:
      print("\nNo one won, house keeps the pot")
      
      
    total_pot -= total_pot
      
    player_choice = input("You wanna continue (Y/n): ")
    print("\n")
    
    if player_choice.lower() == "n":
      print(f"total money : {player_money}")
      break                      
    if player_money <= 0:            
        print("You don't have enough balance – game over!\n")
        return
    
      
gamble()