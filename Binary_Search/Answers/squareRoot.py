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

def mySqrt(x: int) -> int:
    """
    
    Given an number x, return the square root of the number.

    Algorithm:
    - we are sure the sqrt will definitely will be in the range(1,x) that is our search space
    - at mid we will check whether the mid * mid gives us the answer and update the search
    space.

    Args:
        x: input value x
    
    Returns: returns the square root of the number x

    Time Complexity: O(lgx)

    Space Complexity: O(1)

    Pattern: Binary Search

    Subpattern: Binary Search on answers
    """
    if x == 0:
        return 0
    low = 1
    high = x
    ans = 1
    while low  <= high:
        mid = (low + high) // 2

        if mid * mid <= x:
            ans = mid
            low = mid + 1
        else:
            high = mid - 1
    
    return ans

def main():
    # -------------------------
    # WRITE YOUR LOGIC BELOW
    # -------------------------
    x = int(input())
    print('square root of a number:', mySqrt(x))
    return 0

if __name__ == "__main__":
    # Note: These prints will go to output.txt if USE_FILE is True
    main()