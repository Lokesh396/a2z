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

def subsets2( idx, curr, ans, n,arr):
        ans.append(curr[::])
        for i in range(idx,n):
            if idx == i or arr[i-1] != arr[i]:
                curr.append(arr[i])
                subsets2(i+1,curr,ans,n,arr)
                curr.pop()
                
def subsetsWithDup( nums: List[int]) -> List[List[int]]:
    nums.sort()
    ans = []
    subsets2(0,[],ans,len(nums), nums)
    return ans

def main():
    # -------------------------
    # WRITE YOUR LOGIC BELOW
    # -------------------------
    
    return 0

if __name__ == "__main__":
    # Note: These prints will go to output.txt if USE_FILE is True
    main()