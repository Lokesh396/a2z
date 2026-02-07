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

def removeKdigits(num: str, k: int) -> str:
    if k == len(num):
        return '0'
    
    stack  = []
    for digit in num:

        while stack and stack[-1] > digit and k != 0:
            stack.pop()
            k -= 1
        stack.append(digit)

    while k:
        stack.pop()
        k -= 1
    for i in range(len(stack)):
        if stack[i] != '0':
            return "".join(stack[i:])
    
    return '0'

def main():
    # -------------------------
    # WRITE YOUR LOGIC BELOW
    # -------------------------
    
    return 0

if __name__ == "__main__":
    # Note: These prints will go to output.txt if USE_FILE is True
    main()