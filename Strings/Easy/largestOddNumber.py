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

def largestOddNumber(num: str) -> str:
    """
    we need to find the largest odd number in the string.

    Algorithm:
    - we will iterate through the array from back and check whether the char is odd or not, 
    if odd we will return it else decrement right by 1.

    Args:
        num: input number

    Returns: returns the largest odd number.

    Time Complexity: O(n)

    Space Complexity O(1)

    """
    right = len(num)-1

    while right >= 0:
        if int(num[right]) & 1:
            return num[:right+1]
        else:
            right -= 1

    return ""

def main():
    # -------------------------
    # WRITE YOUR LOGIC BELOW
    # -------------------------
    num = input()
    print('larges odd number', largestOddNumber(num))
    return 0

if __name__ == "__main__":
    # Note: These prints will go to output.txt if USE_FILE is True
    main()