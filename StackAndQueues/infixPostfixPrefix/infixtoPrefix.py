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

def reverseAndModify(exp):
    exp = list(exp)
    exp.reverse()
    for i in range(0, len(exp)):
        if exp[i] == ')':
            exp[i]='('
        elif exp[i] =='(':
            exp[i]=')'
    
    return "".join(exp)

def precedence(c):
    if c == '^':
        return 3
    elif c in ['*', '/']:
        return 2
    elif c in ['-', '+']:
        return 1
    
    return 0

def infixPrefix(exp):
    exp = reverseAndModify(exp)
    ans = ''
    stack = []
    for c in exp:
        if ('a' <= c <= 'z') or ('A' <= c <= 'Z') or ('0' <= c <= '9'):
            ans += c

        elif c == '(':
            stack.append('(')
        elif c ==')':
            while stack and stack[-1] !='(':
                ans += stack.pop()
            
            stack.pop()
        else:
            if c == '^':

                while stack and stack[-1] != '(' and precedence(stack[-1]) >= precedence(c):
                    ans += stack.pop()
            else:
                while stack and stack[-1] != '(' and precedence(stack[-1]) > precedence(c):
                    ans += stack.pop()
            stack.append(c)
    
    while stack:
        ans += stack.pop()
    return "".join(list(reversed(ans)))
     
        

def main():
    # -------------------------
    # WRITE YOUR LOGIC BELOW
    # -------------------------
    exp = input()
    print('Infix to prefix', infixPrefix(exp=exp))
    return 0

if __name__ == "__main__":
    # Note: These prints will go to output.txt if USE_FILE is True
    main()