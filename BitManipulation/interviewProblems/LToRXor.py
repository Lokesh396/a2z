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

def findXor1toN(n):

    if n % 4 == 1: return 1
    if n % 4 == 2: return n+1
    if n % 4 == 3: return 0
    
    return n

def findXOR(L : int, R : int) -> int:
    # Write your code here.
    
    oneToL = findXor1toN(L-1)
    onetoR = findXor1toN(R)

    return oneToL ^ onetoR
def main():
    # -------------------------
    # WRITE YOUR LOGIC BELOW
    # -------------------------
    
    return 0

if __name__ == "__main__":
    # Note: These prints will go to output.txt if USE_FILE is True
    main()