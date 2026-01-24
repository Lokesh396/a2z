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

def dfs(idx, curr, csum, n, arr, ans,target):
    if csum == target:
        ans.append(curr[::])
        return
    if idx == n or csum > target:
        return
    
    curr.append(arr[idx])
    dfs(idx, curr, csum+arr[idx],n,arr,ans,target)
    curr.pop()
    dfs(idx+1, curr, csum, n,arr,ans,target)

def combinationSum( candidates: List[int], target: int) -> List[List[int]]:
    
    ans = []
    dfs(0,[],0,len(candidates), candidates,ans,target)
    return ans
def main():
    # -------------------------
    # WRITE YOUR LOGIC BELOW
    # -------------------------
    arr = list(map(int, input().split()))
    k = int(input())
    print(f'All combinations for sum {k}', combinationSum(arr, k))
    return 0

if __name__ == "__main__":
    # Note: These prints will go to output.txt if USE_FILE is True
    main()