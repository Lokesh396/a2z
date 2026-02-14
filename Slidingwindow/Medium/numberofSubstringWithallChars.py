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

def numberOfSubstrings(s: str) -> int:
    
    lastseen = {}
    count = 0
    for i in range(len(s)):
        lastseen[ord(s[i]) -97] = i
        
        if len(lastseen) == 3:
            count += 1 + min(lastseen[0], lastseen[1], lastseen[2])
    
    return count

def main():
    # -------------------------
    # WRITE YOUR LOGIC BELOW
    # -------------------------
    print('number of substrings:', numberOfSubstrings(input()))
    return 0

if __name__ == "__main__":
    # Note: These prints will go to output.txt if USE_FILE is True
    main()