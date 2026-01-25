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

def ispalindrome(s):
    return s == s[::-1]
    
def generate( s, start, curr, ans):
    if start == len(s):
        ans.append(curr[::])
        return
    
    for end in range(start, len(s)):
        currstr = s[start:end+1]
        if ispalindrome(currstr):
            curr.append(currstr)
            generate(s,end+1, curr, ans)
            curr.pop()


def partition( s: str) -> List[List[str]]:
    ans = []
    generate(s,0,[],ans)
    return ans
def main():
    # -------------------------
    # WRITE YOUR LOGIC BELOW
    # -------------------------
    
    return 0

if __name__ == "__main__":
    # Note: These prints will go to output.txt if USE_FILE is True
    main()