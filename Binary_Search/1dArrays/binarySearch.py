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

def binarySearch(arr, target):
    """
    Given an sorted array return the index of the target if it exists.

    Algorithm:
    - we will iterate through the array using the binary search by decreasing the search space by half
    in every iteration.

    Args:
        arr: sorted array
        target: search element
    
    Returns: return the index of the element if its present else -1

    Time Complexity: O(lgn)

    Space Complexity: O(1) no extra space is required.
    """

    low, high = 0, len(arr)-1

    while low <= high:

        mid = (low + high) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1

def main():
    # -------------------------
    # WRITE YOUR LOGIC BELOW
    # -------------------------
    arr = list(map(int, input().split()))
    print('Target presents at:', binarySearch(arr, 9))
    return 0

if __name__ == "__main__":
    # Note: These prints will go to output.txt if USE_FILE is True
    main()