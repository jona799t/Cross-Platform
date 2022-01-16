import sys
import os

def clear():
    os.system('cls' if os.name in ('nt', 'dos') else 'clear')

def title(whatToTitle):
    os.system("title " + whatToTitle) if os.name in ('nt', 'dos') else sys.stdout.write(f"\x1b]2;{whatToTitle}\x07")
