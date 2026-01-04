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

def ceilSArray(arr: List[int], n: int, x: int) -> int:
    """
    You are given an array 'arr' sorted in non-decreasing order and a number 'x'. 
    You must return the index of the largest number in array such that arr[ind] <= x.

    Algorithm:
    - Do a straight forward binary search here we have only two cases
        - less than or equal to
        - else greater than 

    Args:
        arr: sorted input array
        n: length of the array
        x: target element
    
    Returns: returns the index of the ceil of x.

    Time Complexity: O(lgn)

    Space Complexity: O(1)
    """
    low = 0
    high = n-1
    ans = n
    while low <= high:
        mid = (low+high) // 2
        if arr[mid] <= x:
            ans = mid
            low = mid + 1
        else:
            high = mid - 1
    
    return ans
def main():
    # -------------------------
    # WRITE YOUR LOGIC BELOW
    # -------------------------
    arr = list(map(int, input().split()))
    target = int(input())
    print('ceilSArray is at:',ceilSArray(arr, len(arr), target))
    return 0

if __name__ == "__main__":
    # Note: These prints will go to output.txt if USE_FILE is True
    main()