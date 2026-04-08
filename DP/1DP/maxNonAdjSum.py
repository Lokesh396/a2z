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

# Recurrence
def maximumNonAdjacentSumRec(nums):    
    # Write your code here.
    def func(idx):
        if idx >= len(nums):
            return 0
        take = nums[idx] + func(idx+2)
        nottake = func(idx+1)
        return max(take, nottake)
    return func(0)


# Memoization 
def maximumNonAdjacentSum(nums):    
    # Write your code here.
    n = len(nums)
    dp = [0 for _ in range(len(nums))]
    def func(idx):
        if idx < 0:
            return 0
        if dp[idx]:
            return dp[idx]
        take = nums[idx] + func(idx-2)
        nottake = func(idx-1)
        dp[idx] = max(take, nottake)
        return max(take, nottake)
    return func(n-1)

# Tabulation
def maximumNonAdjacentSumTab(nums):    
    # Write your code here.
    n = len(nums)
    if n <= 2:
        return max(nums)
    dp = [0 for _ in range(len(nums))]
    dp[1] = max(nums[0], nums[1])
    for i in range(2, n):
        dp[i] = max(nums[i] + dp[i-2], dp[i-1])
    return dp[n-1]

# Space Optimization
def maximumNonAdjacentSumSpace(nums):    
    # Write your code here.
    n = len(nums)
    if n <= 2:
        return max(nums)
    prev = nums[0]
    curr = max(nums[0], nums[1])
    for i in range(2, n):
        temp = curr
        curr = max(nums[i] + prev, curr)
        prev = temp
    return curr

def main():
    # -------------------------
    # WRITE YOUR LOGIC BELOW
    # -------------------------
    
    return 0

if __name__ == "__main__":
    # Note: These prints will go to output.txt if USE_FILE is True
    main()