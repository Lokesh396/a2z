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

def subsetSum(idx, curr, arr, n, target, ans):
        if target == 0:
            ans.append(curr[::])
            return
        
        for i in range(idx,n):
            if (i == idx or arr[i-1] !=  arr[i]) and target >= arr[i]:
                curr.append(arr[i])
                subsetSum(i+1,curr,arr,n,target-arr[i],ans)
                curr.pop()



def combinationSum2( candidates: List[int], target: int) -> List[List[int]]:
    candidates.sort()
    ans = []
    subsetSum(0,[],candidates, len(candidates), target, ans)
    return ans
def main():
    # -------------------------
    # WRITE YOUR LOGIC BELOW
    # -------------------------
    
    return 0

if __name__ == "__main__":
    # Note: These prints will go to output.txt if USE_FILE is True
    main()