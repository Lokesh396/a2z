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
def singleNumber( nums):
    """
    
    Every number appears twice except that number.

    Algorithm:
    - The xor `^` operator, the `^` of two numbers is zero if they are same as
    same bits becomes 0.

    Args:
        nums: The input array
    
    Returns:
        The element that appeat only once.
    
    Time Complexity: O(n) linear traversal of the array.
    
    Space Complexity: O(1) no extra space is requried.

    """
    output = 0

    for num in nums:
        output = output ^ num
    
    return output
def main():
    # -------------------------
    # WRITE YOUR LOGIC BELOW
    # -------------------------
    arr = list(map(int, input().split()))
    print('Number that didn\'t appear twice:', singleNumber(arr))
    return 0

if __name__ == "__main__":
    # Note: These prints will go to output.txt if USE_FILE is True
    main()