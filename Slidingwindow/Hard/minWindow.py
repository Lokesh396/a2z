import sys
import os
from pathlib import Path
from collections import Counter, defaultdict

# Fast I/O and Recursion Setup
sys.setrecursionlimit(2000)
input = sys.stdin.readline

USE_FILE = True

if USE_FILE:
    BASE_DIR = Path(__file__).resolve().parents[2]
    sys.stdin = open(os.path.join(BASE_DIR, "input.txt"), "r")
    sys.stdout = open(os.path.join(BASE_DIR, "output.txt"), "w")

def minWindow( s: str, t: str) -> str:
        if len(t) > len(s):
            return ''
        tfreq = Counter(t)
        min_len = len(s) + 1
        had = 0
        need = len(tfreq)
        l = 0
        sfreq = defaultdict(int)
        ans = [-1, -1]
        for right in range(len(s)):

            sfreq[s[right]] += 1
            if s[right] in tfreq:
                if tfreq[s[right]] == sfreq[s[right]]:
                    had += 1

            while l <= right and had == need:
                curr_len = right - l +1
                if curr_len < min_len:
                    min_len = curr_len
                    ans = [l, right]
                sfreq[s[l]] -= 1
                if s[l] in tfreq and sfreq[s[l]] < tfreq[s[l]]:
                    had -= 1
                
                if sfreq[s[l]] == 0:
                    del sfreq[s[l]]
                
                l += 1
        if -1 in ans:
            return ''
        return s[ans[0]:ans[1]+1]

def main():
    # -------------------------
    # WRITE YOUR LOGIC BELOW
    # -------------------------
    s = input()
    t = input()

    print('minWindow:', minWindow(s, t))
    return 0

if __name__ == "__main__":
    # Note: These prints will go to output.txt if USE_FILE is True
    main()