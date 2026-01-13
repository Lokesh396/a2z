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
def isIsomorphic(s: str, t: str) -> bool:
    referenceMap = {}
    alreadyPicked = set()
    for i in range(len(s)):
        if s[i] in referenceMap:
            if t[i] != referenceMap[s[i]]:
                return False
        else:
            if t[i] not in alreadyPicked:
                referenceMap[s[i]] = t[i]
                alreadyPicked.add(t[i])
            else:
                return False
    
    return True
def main():
    # -------------------------
    # WRITE YOUR LOGIC BELOW
    # -------------------------
    s = input()
    goal = input()
    print('isAnagram', isIsomorphic(s, goal))
    return 0
    return 0

if __name__ == "__main__":
    # Note: These prints will go to output.txt if USE_FILE is True
    main()