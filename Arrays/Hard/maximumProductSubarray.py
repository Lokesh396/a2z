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


def maxProduct(arr):
    """
    Returns the maximum product over all contiguous subarrays.

    Tracks prefix and suffix products in one pass to handle negative numbers and
    zeros: when a running product hits zero it resets to 1, and we take the best
    among forward and backward products.

    Args:
        arr: List of integers.

    Returns:
        Maximum product value across any contiguous subarray.

    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    prefix = 1
    suffix = 1
    maxi, n = -float('inf'), len(arr)
    for i in range(n):
        if prefix == 0: prefix = 1
        if suffix == 0: suffix = 1
        prefix *= arr[i]
        suffix *= arr[n-i-1]
        maxi = max(maxi, max(prefix, suffix))
    
    return maxi

def main():
    # -------------------------
    # WRITE YOUR LOGIC BELOW
    # -------------------------
    arr = list(map(int, input().split()))
    print('Max Product:', maxProduct(arr=arr))
    return 0

if __name__ == "__main__":
    # Note: These prints will go to output.txt if USE_FILE is True
    main()
