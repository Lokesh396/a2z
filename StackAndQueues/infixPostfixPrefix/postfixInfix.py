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

def postFixInfix(exp):

    stack = []
    for c in exp:
        if c not in ['-', '+', '*', '/', '^']:
            stack.append(c)
        else:
            op1 = stack.pop()
            op2 = stack.pop()
            stack.append(f'({op2}{c}{op1})')
        print(c, stack)
    return stack[0]

def main():
    # -------------------------
    # WRITE YOUR LOGIC BELOW
    # -------------------------
    exp = input()
    print('postfix to infix', postFixInfix(exp))
    return 0

if __name__ == "__main__":
    # Note: These prints will go to output.txt if USE_FILE is True
    main()