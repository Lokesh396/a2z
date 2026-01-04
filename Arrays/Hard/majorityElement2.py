import sys
import os
from pathlib import Path
from math import floor
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
    
    Given an array of numbers, return the elements that appeared than floor of n/3 times

    Algorithm:
    - It works based on the boyer moore's voting algorithm, rather now we take two variables.

    Args:
        nums: input array

    Returns: return the array with majority elements. at max there will be 2 elements.

    Time Complexity: O(n) linear traversal of the input array

    Space Complexity: O(1) here the ouput array size is constant.
    """
    
    minFreq = floor(len(nums) / 3) + 1
    element1, element2 = -float('inf'), -float('inf')
    element1_count, element2_count = 0, 0
    for num in nums:
        if element1_count == 0 and num != element2:
            element1_count += 1
            element1 = num
        elif element2_count == 0 and num != element1:
            element2_count += 1
            element2 = num
        elif element1 == num:
            element1_count += 1
        elif element2 == num:
            element2_count += 1
        else:
            element1_count -= 1
            element2_count -= 1
        
    ans  = []
    if nums.count(element1) >= minFreq:
        ans.append(element1)
    if nums.count(element2) >= minFreq:
        ans.append(element2)

    return ans
def main():
    # -------------------------
    # WRITE YOUR LOGIC BELOW
    # -------------------------
    arr = list(map(int, input().split()))
    print('Majority Elements are:', majorityElement(arr))
    return 0

if __name__ == "__main__":
    # Note: These prints will go to output.txt if USE_FILE is True
    main()