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
def generate_row(n):
        ans = [1]
        prev = 1
        for i in range(1,n):
            prev = prev * (n-i)
            prev = prev // i
            ans.append(prev)
        return ans

        

def generate( numRows):
    ans = []
    for i in range(numRows):
        row = generate_row(i+1)
        ans.append(row)
    return ans

def getElementatRowCol(row, col):
    ans = 1
    for i in range(1,col):
        ans = ans * (row-i)
        ans = ans // i
    return ans
def main():
    # -------------------------
    # WRITE YOUR LOGIC BELOW
    # -------------------------
    n = int(input())
    print('Pascals Triangle:', generate(n))
    print('Row and col Value at 6,4:', getElementatRowCol(6,4))
    return 0

if __name__ == "__main__":
    # Note: These prints will go to output.txt if USE_FILE is True
    main()