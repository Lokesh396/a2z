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
def prefixPostfix(exp):

    stack = []
    for i in range(len(exp)-1, -1, -1):
        c = exp[i]
        if c not in ['-', '+', '*', '/', '^']:
            stack.append(c)
        else:
            op1 = stack.pop()
            op2 = stack.pop()
            stack.append(f'{op1}{op2}{c}')
        print(c, stack)
    return stack[0]
def main():
    # -------------------------
    # WRITE YOUR LOGIC BELOW
    # -------------------------
    s = input()
    print('prefix to postfix:', prefixPostfix(s))
    return 0

if __name__ == "__main__":
    # Note: These prints will go to output.txt if USE_FILE is True
    main()