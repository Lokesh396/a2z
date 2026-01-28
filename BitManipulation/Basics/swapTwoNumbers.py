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

def swapNumber(a:int,  b: int) -> None:
    # write your code here
    a = a ^ b
    b = a ^ b
    a = a ^ b

    return a, b

def main():
    # -------------------------
    # WRITE YOUR LOGIC BELOW
    # -------------------------
    a = int(input())
    b = int(input())
    print('Swap numbers:', swapNumber(a, b))
    return 0

if __name__ == "__main__":
    # Note: These prints will go to output.txt if USE_FILE is True
    main()