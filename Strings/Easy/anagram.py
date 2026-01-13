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
def isAnagram( s: str, goal: str) -> bool:
    if len(s) != len(goal): return False

    hash1 = [0 for i in range(26)]
    hash2 = [0 for i in range(26)]

    for i in range(len(s)):
        hash1[ord(s[i])-97] += 1
        hash2[ord(goal[i])-97] += 1
    
    for i in range(26):
        if hash1[i] != hash2[i]:
            return False
    
    return True
def main():
    # -------------------------
    # WRITE YOUR LOGIC BELOW
    # -------------------------
    s = input()
    goal = input()
    print('isAnagram', isAnagram(s, goal))
    return 0

if __name__ == "__main__":
    # Note: These prints will go to output.txt if USE_FILE is True
    main()