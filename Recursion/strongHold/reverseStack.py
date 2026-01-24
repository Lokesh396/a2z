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

def insert(stack, val):
    if not stack:
        stack.append(val)
        return
    temp = stack.pop()
    insert(stack,val)
    stack.append(temp)

def reverseStack(stack: List[int]) -> None:
    # Write your code here.
    if stack:
        val = stack.pop()
        reverseStack(stack)
        insert(stack, val)
def main():
    # -------------------------
    # WRITE YOUR LOGIC BELOW
    # -------------------------
    
    return 0

if __name__ == "__main__":
    # Note: These prints will go to output.txt if USE_FILE is True
    main()