import sys
import os
from pathlib import Path
from collections import defaultdict

# Fast I/O and Recursion Setup
sys.setrecursionlimit(2000)
input = sys.stdin.readline

USE_FILE = True

if USE_FILE:
    BASE_DIR = Path(__file__).resolve().parents[2]
    sys.stdin = open(os.path.join(BASE_DIR, "input.txt"), "r")
    sys.stdout = open(os.path.join(BASE_DIR, "output.txt"), "w")

def atmostk(s, k):
    left =  0
    right = 0
    cnt = 0
    freqMap = defaultdict(int)
    while right < len(s):
        

        freqMap[s[right]] += 1
        while len(freqMap) > k:
            freqMap[s[left]] -= 1
            if freqMap[s[left]] == 0:
                del freqMap[s[left]]
            left += 1

        cnt += right - left + 1
        right += 1
    return cnt
def countSubStrings(s: str, k: int) -> int:
    # Write your code here
    return atmostk(s, k) - atmostk(s, k-1)

def main():
    # -------------------------
    # WRITE YOUR LOGIC BELOW
    # -------------------------
    s = input()
    print('substrings:', countSubStrings(s, 2))
    return 0

if __name__ == "__main__":
    # Note: These prints will go to output.txt if USE_FILE is True
    main()