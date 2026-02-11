import sys
import os
from pathlib import Path

# Fast I/O and Recursion Setup
sys.setrecursionlimit(2000)
input = sys.stdin.readline

USE_FILE = True

if USE_FILE:
    BASE_DIR = Path(__file__).resolve().parents[2]
    sys.stdin = open(os.path.join(BASE_DIR, "input.txt"), "r")
    sys.stdout = open(os.path.join(BASE_DIR, "output.txt"), "w")
def findCelebrity(n, knows):

    # Write your code here.    
    top = 0
    down = n -1

    while top < down:
        if(knows(top, down)):
            top += 1
        elif(knows(down, top)):
            down -= 1
        else:
            top += 1
            down -= 1
    
    if top < down: return -1

    for i in range(n):
        if i == top:
            continue
        
        if not(knows(i, top) and not knows(top, i)):
            return -1
    
    return top
def main():
    # -------------------------
    # WRITE YOUR LOGIC BELOW
    # -------------------------
    
    return 0

if __name__ == "__main__":
    # Note: These prints will go to output.txt if USE_FILE is True
    main()