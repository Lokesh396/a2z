import sys
import os
from pathlib import Path
from typing import List

# Fast I/O and Recursion Setup
sys.setrecursionlimit(2000)
input = sys.stdin.readline

USE_FILE = True

if USE_FILE:
    BASE_DIR = Path(__file__).resolve().parents[2]
    sys.stdin = open(os.path.join(BASE_DIR, "input.txt"), "r")
    sys.stdout = open(os.path.join(BASE_DIR, "output.txt"), "w")

def twoOddNum(arr : List[int]) -> List[int]:
    # Write your code here.
    xor = 0
    for num in arr:
        xor ^= num
    
    rtsetbit = (xor & (xor-1)) ^ xor

    b1 = 0
    b2 = 0
    for num in arr:

        if num & rtsetbit:
            b1 ^= num
        else:
            b2 ^= num
    
    return [b1, b2] if b1 > b2 else [b2, b1]
def main():
    # -------------------------
    # WRITE YOUR LOGIC BELOW
    # -------------------------
    
    return 0

if __name__ == "__main__":
    # Note: These prints will go to output.txt if USE_FILE is True
    main()