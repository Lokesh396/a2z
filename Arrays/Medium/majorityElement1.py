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
def majorityElement(nums):

    """
    Given an array of elements, there exists an elements which more than n / 2 times, where n is the 
    length of the array.

    Algortithm:
    - It works based on Boyer Moore's counting algorithm.
        - Cancel out different elements pairwise so that if a majority element exists, it remains as the final candidate.
    - If we conside an element as our majority element, every time we see another element if we decrement the count, if the count remains greater than 1, then may be that is the majority element.

    Args:
        nums: Input array

    Time Complexity: O(n) linear traversal of the array.
    Space Complexity: O(1) no extra space is required.
    
    """

    val = 0
    cnt = 0
    for num in nums:
        if cnt == 0:
            val = num
            cnt += 1
        elif val != num:
            cnt -= 1
        else:
            cnt += 1
    
    return val
def main():
    # -------------------------
    # WRITE YOUR LOGIC BELOW
    # -------------------------
    arr = list(map(int, input().split()))
    print('Majority Element: ', majorityElement(arr))
    return 0

if __name__ == "__main__":
    # Note: These prints will go to output.txt if USE_FILE is True
    main()