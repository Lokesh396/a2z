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
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        tsum = sum(nums)
        if tsum & 1:
            return False
        
        target = tsum // 2
        n = len(nums)
        dp = [[-1 for _ in range(target+1)] for _ in range(n)]

        def f(idx,csum):
            if csum == 0:
                return True
            
            if idx < 0:
                return False
            if dp[idx][csum] != -1:
                return dp[idx][csum]
            
            nottake = f(idx-1, csum)
            take = False
            if nums[idx] <= csum:
                take = f(idx-1, csum-nums[idx])
            
            dp[idx][csum] =  (take or nottake)
            return take or nottake
        
        return f(n-1, target)
def main():
    # -------------------------
    # WRITE YOUR LOGIC BELOW
    # -------------------------
    
    return 0

if __name__ == "__main__":
    # Note: These prints will go to output.txt if USE_FILE is True
    main()