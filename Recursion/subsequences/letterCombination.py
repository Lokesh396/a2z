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


def combinations(idx,curr,ans, digits,letterMapping):
    if idx == len(digits):
        ans.append("".join(curr[::]))
        return
    
    chars = letterMapping[digits[idx]]
    for c in chars:
        curr.append(c)
        combinations(idx+1,curr,ans,digits,letterMapping)
        curr.pop()

def letterCombinations( digits: str) -> List[str]:
    letterMapping = {
        '2':'abc',
        '3':'def',
        '4':'ghi',
        '5':'jkl',
        '6':'mno',
        '7':'pqrs',
        '8':'tuv',
        '9':'wxyz'
    }

    ans = []
    combinations(0,[], ans, digits,letterMapping)
    return ans

def main():
    # -------------------------
    # WRITE YOUR LOGIC BELOW
    # -------------------------
    comb = input()
    print(letterCombinations(comb))
    return 0

if __name__ == "__main__":
    # Note: These prints will go to output.txt if USE_FILE is True
    main()