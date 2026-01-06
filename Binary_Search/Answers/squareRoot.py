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

def mySqrt(x: int) -> int:
    if x == 0:
        return 0
    low = 1
    high = x
    ans = 1
    while low  <= high:
        mid = (low + high) // 2

        if mid * mid <= x:
            ans = mid
            low = mid + 1
        else:
            high = mid - 1
    
    return ans

def main():
    # -------------------------
    # WRITE YOUR LOGIC BELOW
    # -------------------------
    x = int(input())
    print('square root of a number:', mySqrt(x))
    return 0

if __name__ == "__main__":
    # Note: These prints will go to output.txt if USE_FILE is True
    main()