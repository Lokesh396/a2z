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

def longestCommonPrefix( strs: List[str]) -> str:
        
    minlen = 201

    for word in strs:
        minlen = min(minlen, len(word))
    
    idx = -1
    for i in range(0,minlen):
        char = strs[0][i]
        cnt = 0
        for word in strs:
            if word[i] == char:
                cnt += 1
        if cnt == len(strs):
            idx = i
        else:
            break
    
    return "" if idx == -1 else strs[0][:idx+1]

def main():
    # -------------------------
    # WRITE YOUR LOGIC BELOW
    # -------------------------
    n = int(input())
    words = []
    for i in range(n):
        words.append(input())
    print('longest common prefix:', longestCommonPrefix(words))
    return 0

if __name__ == "__main__":
    # Note: These prints will go to output.txt if USE_FILE is True
    main()