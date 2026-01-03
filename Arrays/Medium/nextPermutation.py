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
def nextPermutation(nums):
    """
    
    Given an permuation of the array we need to print the next permuatation of that array.

    Algorithm:
    - we traverse from the left and find the index where we can see a dip.
    - if that index is -1, that means that the last permuatation of the array, and simply reverse and return
    - we need to find the element which is greater than the element at the index and swap them
    and simply reverse the elements from that index.

    Args:
        nums: input array
    
    Returns: next permutation will be there inplace.

    Time Complexity: O(n), traversals and reverse will take at max o(n) time

    Space Complexity: O(1), no extra space is required

    """
    n = len(nums)
    ind = -1
    for i in range(n-2, -1, -1):
        if nums[i] < nums[i+1]:
            ind = i
            break
    if ind == -1:
        nums.reverse()
        return
    
    for i in range(n-1, ind, -1):
        if nums[i] > nums[ind]:
            nums[i], nums[ind] = nums[ind], nums[i]
            break
    ind += 1
    while ind < n-1:
        nums[ind], nums[n-1] = nums[n-1], nums[ind]
        ind += 1
        n -= 1
        
def main():
    # -------------------------
    # WRITE YOUR LOGIC BELOW
    # -------------------------
    arr = list(map(int, input().split()))
    nextPermutation(arr)
    print('Next Permuatation: ', *arr)
    return 0

if __name__ == "__main__":
    # Note: These prints will go to output.txt if USE_FILE is True
    main()