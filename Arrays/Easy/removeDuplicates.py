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

def remove_duplicates(arr):
    """
    Remove duplicates from a sorted list in-place using a two-pointer sweep.

    Algorithm:
    - Keep `l` at the position of the last unique element and `r` as a scanner.
    - When `arr[l]` differs from `arr[r]`, advance `l` and copy the new unique
      value from `r` into `arr[l]`.
    - After one pass, the first `l + 1` positions store the unique values.

    Args:
        arr: Sorted list of hashable items with possible duplicates.

    Returns:
        Index of the last unique element (equivalently, unique count minus one).

    Time Complexity: O(n) for a single traversal of the list.
    Space Complexity: O(1) extra space; the list is modified in-place.
    """
    l, r = 0, 0

    while r < len(arr):
        if arr[l] != arr[r]:
            print(f"left: {l}, right: {r}, arr[l]: {arr[l]}, arr[r]: {arr[r]}")
            arr[l+1] = arr[r]
            l += 1
        
        r += 1
    print(arr)
    return l

def main():
    # -------------------------
    # WRITE YOUR LOGIC BELOW
    # -------------------------
    arr = list(map(int, input().split()))
    print('upto index: ', remove_duplicates(arr=arr))
    return 0

if __name__ == "__main__":
    # Note: These prints will go to output.txt if USE_FILE is True
    main()
