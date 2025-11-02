import random
import sys
import os

sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), "Games"))

score = 0 

def clear_screen():
	os.system('clear')

def math_quiz():
    global score
    clear_screen()
    
    print("--------- | Math Quiz | ---------")
    
    while True:
        num = list(range(1, 99))
        a = random.choice(num)
        b = random.choice(num)
        
        operations = ['+', '*', '-']
        op = random.choice(operations)
        
        if op == "+":
            print(f"| {a} {op} {b} |")
            result = a + b
        elif op == "*":
            print(f"| {a} {op} {b} |")
            result = a * b
        elif op == "-":
            print(f"| {a} {op} {b} |")
            result = a - b
        
        answer = int(input("Answer: "))
        if answer == result:
            print("Correct")
            score += 1  
            print(f"Score: {score}")
            print("exit or continue?")
            cho = input("player: ").lower()
            if cho == "exit":
                import gamelibrary
                gamelibrary.main()
            else:
                math_quiz()
        else:
            print("Incorrect")
            