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
def isValid(s: str) -> bool:
    stack = []
    polarityMap = {
        '}':'{',
        ']':'[',
        ')':'('
    }
    for c in s:
        if c in ['(', '[', '{']:
            stack.append(c)
        elif not stack or stack[-1] != polarityMap[c]:
                return False
        else:
            stack.pop()

    return not stack
def main():
    # -------------------------
    # WRITE YOUR LOGIC BELOW
    # -------------------------
    s = input()
    print('valid parentheses ', isValid(s))
    return 0

if __name__ == "__main__":
    # Note: These prints will go to output.txt if USE_FILE is True
    main()