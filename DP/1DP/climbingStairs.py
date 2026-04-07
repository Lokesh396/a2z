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

            
def climbStairs(n: int) -> int:
    if n < 2:
        return 1
    cached = [0 for i in range(n+1)]
    cached[1] = 1
    cached[2] = 2
    for i in range(3, n+1):
        cached[i] = cached[i-1] + cached[i-2]
    return cached[n]
def main():
    # -------------------------
    # WRITE YOUR LOGIC BELOW
    # -------------------------
    n = int(input())
    print('ways:', climbStairs(n))
    return 0

if __name__ == "__main__":
    # Note: These prints will go to output.txt if USE_FILE is True
    main()