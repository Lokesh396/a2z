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

def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        
    stack = []

    for i in range(len(asteroids)):
        
        stack.append(asteroids[i])

        while stack and len(stack) >= 2 and stack[-1] <0 and stack[-2] > 0:
            top1 = stack.pop()
            top2 = stack.pop()
            if abs(top1) != abs(top2):
                newval = max(abs(top1), abs(top2))
                if newval == abs(top1) and top1 < 0:
                    stack.append(-newval)
                elif newval == abs(top2) and top2 < 0:
                    stack.append(-newval)
                else:
                    stack.append(newval)

    return stack

def main():
    # -------------------------
    # WRITE YOUR LOGIC BELOW
    # -------------------------
    
    return 0

if __name__ == "__main__":
    # Note: These prints will go to output.txt if USE_FILE is True
    main()