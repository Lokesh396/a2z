import sys
import os
from pathlib import Path
from math import ceil
from typing import List

# Fast I/O and Recursion Setup
sys.setrecursionlimit(2000)
input = sys.stdin.readline

USE_FILE = True

if USE_FILE:
    BASE_DIR = Path(__file__).resolve().parents[2]
    sys.stdin = open(os.path.join(BASE_DIR, "input.txt"), "r")
    sys.stdout = open(os.path.join(BASE_DIR, "output.txt"), "w")

def divisorSum(nums,mid):
    """
    Given the nums array and mid, return the sum if all the nums is divided by mid and added.

    Algorithm:
    - divide each number with the mid and sum up the result.

    Args:
        nums: input array 
        mid: divisor
    
    Returns: returns the divisor sum

    Time Complexity: O(n)

    Space Complexity: O(1)
    """
    total = 0
    
    for num in nums:
        total += ceil(num / mid)
    return total

def smallestDivisor(nums: List[int], threshold: int) -> int:
    
    """
    
    Given the array and nums and the thershold, reurn the smallest divisor, if we divde all 
    the numbers and sum up the result that will be less than or equal to the threshold.

    Algorithm:
    - the search space from (1, max(nums))
    - we will do a binary search on that search space and check whether if that is possible to
    get the threshold.

    Args:
        nums: input array
        threshold: the threshold
    
    Returns: reutrn the smallest divisor

    Time Complexity: O(lg(max(nums) * n))

    Space CoPmplexity: O(1)

    Pattern: Binary Search

    SubPatterns: Binary search on answers. (possible or not possible)
    """
    low = 1
    high = max(nums)
    ans = -1
    while low <= high:

        mid = (low + high) // 2

        total = divisorSum(nums, mid)

        if total <= threshold:
            ans = mid
            high = mid - 1
        else:
            low = mid + 1
    
    return ans

def main():
    # -------------------------
    # WRITE YOUR LOGIC BELOW
    # -------------------------
    arr = list(map(int, input().split()))
    threshold = int(input())
    print('Smallest divisor:', smallestDivisor(arr, threshold))
    return 0

if __name__ == "__main__":
    # Note: These prints will go to output.txt if USE_FILE is True
    main()