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
def subsets(idx, arr, n, k,curr,csum,ans):
    if len(curr) == k or idx == len(arr):
        if csum == n and len(curr) == k:
            ans.append(curr[::])
        return
    
    curr.append(arr[idx])
    subsets(idx+1,arr,n,k,curr,csum+arr[idx], ans)
    curr.pop()
    subsets(idx+1,arr,n,k,curr,csum, ans)


            

def combinationSum3( k: int, n: int) -> List[List[int]]:
    candidates  = [1,2,3,4,5,6,7,8,9]
    ans = []
    subsets(0,candidates,n,k,[],0,ans)
    return ans
def main():
    # -------------------------
    # WRITE YOUR LOGIC BELOW
    # -------------------------
    k = int(input())
    n = int(input())
    ans = combinationSum3(k, n)
    print(ans)
    return 0

if __name__ == "__main__":
    # Note: These prints will go to output.txt if USE_FILE is True
    main()