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


def optimal(arr, k):
    """
    
    Given an array and sum k, we need to return the maximum length of the array that sums to k.

    Algorithm:
     - we will add the current to the sum, in any point of time if sum becomes greater than k,
    we will subract from left.

    Args:
        arr: Input array
        k: target sum
    
    Returns:
        It will the return the length of maximum subarray with k.
    
    Time Complexity: O(n) two pointers l and r traverse through the array at most 2n times

    Space Complexity: O(1) no extra space is required.
        
    """

    n = len(arr)
    left, right = 0, 0
    maxLen = 0
    csum = arr[0]

    while right < n:

        while csum >k and left <= right:
            csum -= arr[left]
            left += 1
        
        if csum == k:
            maxLen = max(maxLen, right - left + 1)

        right += 1
        if right < n:
            csum += arr[right]

    
    return maxLen

def main():
    # -------------------------
    # WRITE YOUR LOGIC BELOW
    # -------------------------
    arr = list(map(int, input().split()))
    k = int(input())
    print('The length of the longest Subarray with sum K: ', optimal(arr=arr, k=k))
    return 0

if __name__ == "__main__":
    # Note: These prints will go to output.txt if USE_FILE is True
    main()