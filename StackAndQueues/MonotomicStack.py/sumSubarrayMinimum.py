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

    def nse(self, arr):
        n = len(arr)
        stack = []
        ans = [n for i in range(n)]

        for i in range(n-1, -1, -1):

            while stack and arr[stack[-1]] >= arr[i]:
                stack.pop()
            
            if stack:
                ans[i] = stack[-1]
            stack.append(i)
        return ans

    def pseq(self, arr):
        n = len(arr)
        stack = []
        ans = [-1 for i in range(n)]

        for i in range(n):

            while stack and arr[stack[-1]] > arr[i]:
                stack.pop()
            
            if stack:
                ans[i] = stack[-1]
            stack.append(i)

        return ans


    def sumSubarrayMins(self, arr: List[int]) -> int:
        
        MOD = 1e9 + 7
        total = 0
        nse = self.nse(arr)
        pseq = self.pseq(arr)

        for i in range(len(arr)):

            ps = i - pseq[i]
            ns = nse[i] - i
            freq = ps * ns
            subarrays= (freq *  arr[i]) % MOD
            total = (total +  subarrays ) % MOD
        
        return  int(total % MOD)

def main():
    # -------------------------
    # WRITE YOUR LOGIC BELOW
    # -------------------------
    
    return 0

if __name__ == "__main__":
    # Note: These prints will go to output.txt if USE_FILE is True
    main()