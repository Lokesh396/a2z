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
def moveZeroes(nums):
        """
        Move all the zeroes in the array to the last

        Algorithm:
        - we need to find the first zero index and place pointer `l` at that position
        - If we encounter any non zero element and the `l` has a valid zero index
        swap elements at `l` and `r`.

        Args:
            nums: input array that contains zero elements.
        
        Time Complexity: O(n) Two pointer approach single iteration.
        
        Space Complexity: O(1) Only some variables.
        """
        l = -1
        r = 0
        while r < len(nums):
            if nums[r] == 0 and l == -1:
                l = r
            
            elif nums[r] != 0 and l != -1:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
            
            r += 1

def main():
    # -------------------------
    # WRITE YOUR LOGIC BELOW
    # -------------------------
    arr = list(map(int, input().split()))
    print(arr, "Before moving zeroes")
    moveZeroes(arr)
    print(arr, "After moving zeroes")
    return 0

if __name__ == "__main__":
    # Note: These prints will go to output.txt if USE_FILE is True
    main()