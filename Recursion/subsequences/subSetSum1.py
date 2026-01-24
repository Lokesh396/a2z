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

def subsets(idx,csum,arr, n, ans):
    if idx == n:
        ans.append(csum)
        return
    subsets(idx+1, csum+arr[idx], arr, n, ans)
    subsets(idx+1, csum, arr, n, ans)
    
def subsetSum(num: List[int]) -> List[int]:
    # Write your code here.
    ans = []
    subsets(0,0,num, len(num),ans)
    ans.sort()
    return ans
def main():
    # -------------------------
    # WRITE YOUR LOGIC BELOW
    # -------------------------
    arr = list(map(int, input().split()))
    print('subset sum:', subsetSum(arr))
    return 0

if __name__ == "__main__":
    # Note: These prints will go to output.txt if USE_FILE is True
    main()