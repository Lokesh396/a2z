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

def allstrings(prev, ans, n):
    """
    we need to generate all the substring of size n, where there will
    be no consective 0 in the string.

    Algorithm:
     - the base cases are if we the current generated string length is 2, we need to verify
     whether the last two characthers contains only zeroes, if they are we need to reutrn early
     - if we reach n so that means we crated one valid substring of size we append that to our ans
     and return.
     - we have two choices either we can add 0 or 1 to our already previous string.

     Args:
        prev : string that constructed so far
        ans: lst to store the answer
        n: legnth of the substring.

    Returns: returns the vaid substrings.

    Time Complexity: O(2^n)

    Space Complexity :O(n)
    """
    if len(prev) >= 2:
        if prev[-1] == '0' and prev[-2] == '0':
            return
    if len(prev) == n:
        ans.append(prev)
        return
    allstrings(prev+'0',ans, n)
    allstrings(prev+'1', ans, n)

def validStrings( n: int) -> List[str]:
    ans = []
    allstrings('', ans, n)
    return ans
def main():
    # -------------------------
    # WRITE YOUR LOGIC BELOW
    # -------------------------
    n = int(input())
    print('allstrings', validStrings(n))
    return 0

if __name__ == "__main__":
    # Note: These prints will go to output.txt if USE_FILE is True
    main()