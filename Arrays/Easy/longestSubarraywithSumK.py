import sys
import os
from pathlib import Path
from collections import defaultdict
# Fast I/O and Recursion Setup
sys.setrecursionlimit(2000)
input = sys.stdin.readline

USE_FILE = True

if USE_FILE:
    BASE_DIR = Path(__file__).resolve().parents[2]
    sys.stdin = open(os.path.join(BASE_DIR, "input.txt"), "r")
    sys.stdout = open(os.path.join(BASE_DIR, "output.txt"), "w")


def sumEqualsK(arr, k):
    """
    
    Given an array and sum k, we need to return the maximum length of the array that sums to k.

    Algorithm:
    - Suppose we are at x, and the sum is csum, if we need to whether k exists upto that array,
    we need to check does csum-x present in hashmap. as csum -x + x = csum.
    - we store the csum in to the dictinoary if it is not already present it the dictionaty as
    we need to find the maximum length.

    Args:
        arr: input array may contains negatives.
        k: target sum

    Returns:
        Return the maximum lenght of the subarray with sum k
    
    Time Complexity: O(n) Single iteration of the array, as the amoritized complexity of
    lookup and insertion in hashmap is O(1).

    Space Complexity: O(n) If the array contains all the unique elements we need to store 
    the sum of all elements up to last index.

    """
    preMap = defaultdict(int)
    csum = 0
    maxLen = 0
    for idx, num in enumerate(arr):
        csum += num

        if csum == k:
            maxLen = max(maxLen, idx + 1)
        
        if csum not in preMap:
            preMap[csum] = idx
        
        if csum - k in preMap:
            maxLen = max(maxLen, idx-preMap[csum-k])

    
    return maxLen
         

def main():
    # -------------------------
    # WRITE YOUR LOGIC BELOW
    # -------------------------
    arr = list(map(int, input().split()))
    k = int(input())
    print('The length of the longest Subarray with sum K: ', sumEqualsK(arr=arr, k=k))
    return 0

if __name__ == "__main__":
    # Note: These prints will go to output.txt if USE_FILE is True
    main()