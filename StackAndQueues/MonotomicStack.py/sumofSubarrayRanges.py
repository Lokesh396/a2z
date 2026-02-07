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
        nse = [n for i in range(n)]
        stack = []

        for i in range(n-1, -1, -1):

            while stack and arr[stack[-1]] >= arr[i]:
                stack.pop()
            
            if stack:
                nse[i] = stack[-1]
            stack.append(i)

        return nse
    def pseq(self, arr):
        n = len(arr)
        nse = [-1 for i in range(n)]
        stack = []

        for i in range(n):

            while stack and arr[stack[-1]] > arr[i]:
                stack.pop()
            
            if stack:
                nse[i] = stack[-1]
            stack.append(i)

        return nse
    def nge(self, arr):
        n = len(arr)
        nse = [n for i in range(n)]
        stack = []

        for i in range(n-1, -1, -1):

            while stack and arr[stack[-1]] <= arr[i]:
                stack.pop()
            
            if stack:
                nse[i] = stack[-1]
            stack.append(i)

        return nse
    def pgeq(self, arr):
        n = len(arr)
        nse = [-1 for i in range(n)]
        stack = []

        for i in range(n):

            while stack and arr[stack[-1]] < arr[i]:
                stack.pop()
            
            if stack:
                nse[i] = stack[-1]
            stack.append(i)

        return nse

    def sumOfLargest(self, nums): 
        nge = self.nge(nums)
        pgeq = self.pgeq(nums)
        total = 0
        for i in range(len(nums)):
            left =  i - pgeq[i]
            right = nge[i] - i

            total += (left * right * nums[i])
        
        return total
    
    def sumOfSmallest(self, nums): 
        nge = self.nse(nums)
        pgeq = self.pseq(nums)
        total = 0
        for i in range(len(nums)):
            left =  i - pgeq[i]
            right = nge[i] - i

            total += (left * right * nums[i])
        
        return total

    def subArrayRanges(self, nums: List[int]) -> int:
        return self.sumOfLargest(nums) - self.sumOfSmallest(nums)
       

def main():
    # -------------------------
    # WRITE YOUR LOGIC BELOW
    # -------------------------
    arr = list(map(int, input().split()))
    solution = Solution()
    print('sum of subarray ranges:',solution.subArrayRanges(arr))
    return 0

if __name__ == "__main__":
    # Note: These prints will go to output.txt if USE_FILE is True
    main()