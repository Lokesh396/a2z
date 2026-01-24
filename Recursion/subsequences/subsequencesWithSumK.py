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

def countsubsequences(idx,csum,arr, n, target):
    if idx == n:
        if csum == target:
            return 1
        return 0
    
    take = countsubsequences(idx+1,csum+arr[idx], arr, n, target)
    nottake = countsubsequences(idx+1,csum, arr, n, target)

    return take + nottake
def main():
    # -------------------------
    # WRITE YOUR LOGIC BELOW
    # -------------------------
    arr = list(map(int, input().split()))
    k = int(input())
    ans = []
    count = countsubsequences(0,0,arr,len(arr), k)
    print(f'All subsequences with sum k {k}:', count)
    return 0

if __name__ == "__main__":
    # Note: These prints will go to output.txt if USE_FILE is True
    main()