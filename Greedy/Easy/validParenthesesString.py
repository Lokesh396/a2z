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
def checkValidString(s: str) -> bool:
        min_r = 0
        max_r = 0

        for c in s:
            if c == '(':
                min_r += 1
                max_r += 1
            elif c == ')':
                min_r -= 1
                max_r -= 1
            else:
                min_r -= 1
                max_r += 1
            
            if min_r < 0: min_r = 0
            if max_r <0 : return False
        
        return min_r == 0

def main():
    # -------------------------
    # WRITE YOUR LOGIC BELOW
    # -------------------------
    print('valid string:', checkValidString(input()))
    return 0

if __name__ == "__main__":
    # Note: These prints will go to output.txt if USE_FILE is True
    main()