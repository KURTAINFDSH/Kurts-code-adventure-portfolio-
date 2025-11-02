import sys
from rich import print
from time import sleep

#line blue
def blue():
    lines = [
        ("your morning eyes-", 0.10),
        ("I could stare like watching stars", 0.1),
        ("I could walk you by-", 0.10),
        ("and ill tell without a thought", 0.08),
        ("you'd be mine ", 0.08),
        ("would you mind", 0.08),
        ("if i took your hand tonight", 0.10),
        ("know you're' all", 0.10),
        ("that i want",0.13),
        ("this life", 0.13),
        ("ill imagine we fell in love", 0.10),
        ("ill nap under moonlight skies with you", 0.10),
    ]

    delays = [1, 1, 1, 1.5, 0.8, 0.18, 0.5, 0.10, 0.19, 3, 0.5, 0.3, 0.3, 0.1, 5]

    for i, (line, char_delay) in enumerate(lines):
        for char in line:
            if line == "ill imagine we fell in love":
                print(f"[cyan]{char}[/cyan]", end="")
            elif line == "ill nap under moonlight skies with you":
                print(f"[cyan]{char}[/cyan]", end="")
            else:
                print(f"[bold white3]{char}[/bold white3]", end="")
            sys.stdout.flush()
            sleep(char_delay)
        print()  # new line after finishing the line
        sleep(delays[i])

# to run
blue()