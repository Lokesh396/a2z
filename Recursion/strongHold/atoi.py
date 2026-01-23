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
    
def strtoint(s, i, final, sign) -> List[int]:
    if i >= len(s):
        return [final, sign]
    

    if s[i] in ('+', '-') and sign == 0 and final == 0 and i == 0:
        sign = 1 if s[i] == '+' else -1 
        i += 1
        return strtoint(s, i, final, sign)
    elif s[i].isdigit():
        final = final * 10 + int(s[i])
        i+= 1
        return strtoint(s, i, final, sign)
    else:
        return [final, sign]
    


def myAtoi( s: str) -> int:
    s = s.strip()
    [final, sign] =  strtoint(s,0,0, 0)
    if sign == -1:
        return max(-int(final), -2**31)
    return min(int(final),(2**31)-1)

def main():
    # -------------------------
    # WRITE YOUR LOGIC BELOW
    # -------------------------
    
    return 0

if __name__ == "__main__":
    # Note: These prints will go to output.txt if USE_FILE is True
    main()