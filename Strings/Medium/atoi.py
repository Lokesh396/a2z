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

def myAtoi(s: str) -> int:
    """
    Given a string representation of integer we need to return a valid integer from the string that
    can be formed.

    Algorithm:
    - we will strip the white spaces from the string and iterate through the string.
    - if we encounter a sign it should be the first characther it should not appear in the middle.
    - if we encounter a zero it should be in the middle as prefix zeroes has no significance.
    - if we encounter a non digit we will break out.

    Args:
        - s: input string
    
    Returns: return the length of the maximum valid string.

    Time Complexity: O(n)
    
    Space Complexity: O(1)
    """
    
    final = ""
    sign = ''
    s = s.strip()
    for c in s:
        if c == '-' or c == '+':
            if final=="" and sign == "":
                sign = c
                continue
            else:
                break

        if c == '0' and final !="":
            final += '0'
            continue
        if c.isdigit():
            final += c

        else:
            break
    
    if final == "":
        return 0
    
    if sign == '-':
        return max(-int(final),-2**31)
    else:
        return min(int(final), 2**31-1)
    
def main():
    # -------------------------
    # WRITE YOUR LOGIC BELOW
    # -------------------------
    s = input()
    print('Atoi:', myAtoi(s))
    return 0

if __name__ == "__main__":
    # Note: These prints will go to output.txt if USE_FILE is True
    main()