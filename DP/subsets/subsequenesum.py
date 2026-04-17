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

def subsetSumToK(n, k, arr):

    # Write your code here
    # Return a boolean variable 'True' or 'False' denoting the answer
    dp = [[-1 for _ in range(k+1)] for _ in range(n)]
    def f(idx,s):
        if s == 0:
            return True
        if idx < 0:
            return False
        if dp[idx][s] != -1:
            return dp[idx][s]
        nottake = f(idx-1, s)
        take = False
        if arr[idx]  <= s:
            take = f(idx-1, s-arr[idx])
        dp[idx][s] = take or nottake
        return take or nottake

    return f(n-1, k)   
def main():
    # -------------------------
    # WRITE YOUR LOGIC BELOW
    # -------------------------
    
    return 0

if __name__ == "__main__":
    # Note: These prints will go to output.txt if USE_FILE is True
    main()