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

def NthRoot(n: int, m: int) -> int:
    # Write Your Code Here
    low = 1
    high = m

    while low <= high:
        
        mid = (low+high)//2

        currval = mid ** n
        if currval == m:
            return mid
        
        elif currval < m:
            low = mid + 1
        else:
            high = mid -1
    
    return -1

def main():
    # -------------------------
    # WRITE YOUR LOGIC BELOW
    # -------------------------
    n = int(input())
    m = int(input())
    print('Nth root of m is:', NthRoot(n, m))
    return 0

if __name__ == "__main__":
    # Note: These prints will go to output.txt if USE_FILE is True
    main()