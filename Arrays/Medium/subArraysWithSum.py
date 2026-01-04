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

def subarraySum(nums, k):
    """
    
    Given an array of nums, and a target sum k, we need to count the no. of subarrays that 
    sum up to the k.

    Algorithm:
    - For each index, I check how many times I've seen a prefix sum equal to 
    currentSum - k, because each such occurrence forms a subarray ending here with sum k

    Args:
        nums: input array
        k   : target sum
    
    Retruns: returns the count of subarrays that sums to k.

    Time Complexity: O(n) for linear traversal of the array.

    Space Complexity: O(n) for storing all the prefix sums.
    """
    prefixMap = {0:1}
    preSum = 0
    count = 0
    for num in nums:
        preSum += num
        count += prefixMap.get(preSum-k, 0)
        prefixMap[preSum] = prefixMap.get(preSum, 0) + 1
    
    return count
def main():
    # -------------------------
    # WRITE YOUR LOGIC BELOW
    # -------------------------
    arr = list(map(int, input().split()))
    target = int(input())
    print(f'count of Subarrays with the target {target}: ', subarraySum(arr, target))
    return 0

if __name__ == "__main__":
    # Note: These prints will go to output.txt if USE_FILE is True
    main()