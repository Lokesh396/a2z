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
def isExists(idx, csum, arr, n, k):
    if idx == n:
        if csum == k:
            return True
        return False
    
    take = isExists(idx+1, csum+arr[idx], arr, n, k)
    if take: return True
    nottake = isExists(idx+1, csum, arr, n, k)
    if nottake: return True

    return False

def subsetSumToK(n, k, arr):

    # Write your code here
    # Return a boolean variable 'True' or 'False' denoting the answer
    return isExists(0,0,arr,n,k)
def main():
    # -------------------------
    # WRITE YOUR LOGIC BELOW
    # -------------------------
    arr = list(map(int, input().split()))
    k = int(input())
    print(f'subset with sum {k} exists:', subsetSumToK(len(arr), k, arr))
    return 0

if __name__ == "__main__":
    # Note: These prints will go to output.txt if USE_FILE is True
    main()