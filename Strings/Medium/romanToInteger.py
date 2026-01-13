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

def romanToInt(s: str) -> int:
    romanmap = {
        'I':1,
        'V':5,
        'X':10,
        'L':50,
        'C':100,
        'D':500,
        'M':1000,
        'IV':4,
        'IX':9,
        'XC':90,
        'XL':40,
        'CD':400,
        'CM':900
    }
    right = len(s)-1
    total = 0
    while right >= 0:
        
        if right > 0 and s[right-1:right+1] in romanmap:
            total += romanmap.get(s[right-1:right+1], 0)
            right -= 2
        else:
            total += romanmap.get(s[right], 0)
            right -= 1
        
    return total

def main():
    # -------------------------
    # WRITE YOUR LOGIC BELOW
    # -------------------------
    s = input()
    print('Roman to Integer:', romanToInt(s))
    return 0

if __name__ == "__main__":
    # Note: These prints will go to output.txt if USE_FILE is True
    main()