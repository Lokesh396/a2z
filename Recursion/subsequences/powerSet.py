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

def generate( nums, idx, curr, ans):
    """

    We are given an list of size n, we generate all the possible subsequences.

    Algorithm:
        - at every step we have two choices take the current element or skip it
        - we backtrack everytime after take the element we remove it from our solution.
        - if the current index equal len(nums), a solution has been constructed, we
        append that to our solution and returns.
    
    Args:
        nums: input array
        idx : curr index
        curr: current formed solution
        ans: list storing subsequences

    Returns: return the array of subsequences

    Time Complexity: O(2^n)

    Space Complexity: O(n)

    """
    if idx >= len(nums):
        ans.append(curr[::])
        return
    
    curr.append(nums[idx])
    generate(nums, idx+1, curr, ans)
    curr.pop()
    generate(nums, idx+1, curr, ans)
def subsets( nums: List[int]) -> List[List[int]]:
    ans = []
    generate(nums, 0, [], ans)
    return ans

def main():
    # -------------------------
    # WRITE YOUR LOGIC BELOW
    # -------------------------
    nums = list(map(int, input().split()))
    subset = subsets(nums)
    print(len(subset))
    print(f'All subsets for {nums}:',subset)
    return 0

if __name__ == "__main__":
    # Note: These prints will go to output.txt if USE_FILE is True
    main()