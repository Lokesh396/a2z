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

def romanToInt(s: str) -> int:
    """
    Given a string which is a roman numeral, we need to return the integer representation of the roman
    numeral.

    Algorithm:
    - we start traversing the string from right and check for last 2 chars whether it is presnet in our
    roman map if  it is present we will add that too our total and decrement by 2.
    - else we add the last char value to the total.

    Args:
        - s: string representation of roman number
    
    Returns: returns the integer

    Time Complexity: O(n)

    Space Complexity: O(1)
    """
    romanmap = {
        'I':1,
        'V':5,
        'X':10,
        'L':50,
        'C':100,
        'D':500,
        'M':1000,
        'IV':4,
        'IX':9,
        'XC':90,
        'XL':40,
        'CD':400,
        'CM':900
    }
    right = len(s)-1
    total = 0
    while right >= 0:
        
        if right > 0 and s[right-1:right+1] in romanmap:
            total += romanmap.get(s[right-1:right+1], 0)
            right -= 2
        else:
            total += romanmap.get(s[right], 0)
            right -= 1
        
    return total

def main():
    # -------------------------
    # WRITE YOUR LOGIC BELOW
    # -------------------------
    s = input()
    print('Roman to Integer:', romanToInt(s))
    return 0

if __name__ == "__main__":
    # Note: These prints will go to output.txt if USE_FILE is True
    main()