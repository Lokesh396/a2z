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

def first(arr, n,k):
    """
    Given an array of size n, return the first occurence of the target k

    Algorithm:
    - we will do normal binary search, if a element is found we need to go left to find the first
    occurence.

    Args:
        arr: input array
        n: length of the array
        k: target
    
    returns: returns the first occurence of the element if exists else -1

    """
    low = 0
    high = n -1
    ans = -1
    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == k:
            ans = mid
            high = mid -1
        elif arr[mid] > k:
            high = mid - 1
        else:
            low = mid + 1
    return ans

def last(arr, n,k):
    """
    Given an array of size n, return the last occurence of the target k

    Algorithm:
    - we will do normal binary search, if a element is found we need to go right to find the last
    occurence.

    Args:
        arr: input array
        n: length of the array
        k: target
    
    Returns: returns the last occurence of the element if exists else -1

    Time Complexity: O(lgn)

    Space Complexity: O(1)
    """
    low = 0
    high = n -1
    ans = -1
    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == k:
            ans = mid
            low = mid +1
        elif arr[mid] > k:
            high = mid - 1
        else:
            low = mid + 1
    return ans
def count(arr: List[int], n: int, x: int) -> int:
    # Your code goes here
    fst = first(arr, n, x)
    if fst == -1: return 0
    lst = last(arr, n, x)
    return lst - fst + 1

def main():
    # -------------------------
    # WRITE YOUR LOGIC BELOW
    # -------------------------
    arr = list(map(int, input().split()))
    target = int(input())
    print('Occurence Count:', count(arr, len(arr), target))
    return 0

if __name__ == "__main__":
    # Note: These prints will go to output.txt if USE_FILE is True
    main()