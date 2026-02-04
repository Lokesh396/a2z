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

def precedence(c):
    if c == '^':
        return 3
    elif c == '/' or c == '*':
        return 2
    if c == '+' or c == '-':
        return 1
    else:
        return -1

def infixToPostfix(exp: str) -> str:
    postfix = ''
    stack = []
    for c in exp:
        if ('a' <= c <= 'z') or ('A' <= c <= 'Z') or ('0' <= c <= '9'):
            postfix += c
        elif c == '(':
            stack.append('(')
        
        elif c == ')':
            while stack and stack[-1] != '(':
                postfix += stack.pop()
            
            stack.pop()
        else:
            while stack and stack[-1] != '(' and (precedence(stack[-1]) >= precedence(c)):
                postfix += stack.pop()
            stack.append(c)
    while stack:
        postfix += stack.pop()

    return postfix
def main():
    # -------------------------
    # WRITE YOUR LOGIC BELOW
    # -------------------------
    
    return 0

if __name__ == "__main__":
    # Note: These prints will go to output.txt if USE_FILE is True
    main()