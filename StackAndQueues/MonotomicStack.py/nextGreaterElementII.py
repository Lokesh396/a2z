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

def nextGreaterElementsOptimized( nums: List[int]) -> List[int]:
    n = len(nums)
    stack = []
    ans = [-1 for i in range(n)]

    for i in range(2*n-1, -1, -1):
        idx = i % n
        num = nums[idx]
        while stack and stack[-1] <= num:
            stack.pop()
        if i < n:
            if stack:
                ans[idx] = stack[-1]
        
        
        stack.append(num)
    
    return ans

def nextGreaterElements( nums: List[int]) -> List[int]:
    n = len(nums)
    nums = nums + nums
    nums.pop()
    stack = []
    ans = []

    for i in range(len(nums)-1, -1, -1):
        num = nums[i]
        while stack and stack[-1] <= num:
            stack.pop()
        
        if stack:
            ans.append(stack[-1])
        else:
            ans.append(-1)
        
        stack.append(num)
    
    ans.reverse()
    return ans[:n]

def main():
    # -------------------------
    # WRITE YOUR LOGIC BELOW
    # -------------------------
    arr  = list(map(int, input().split()))
    print('next greater element II:', nextGreaterElementsOptimized(arr))
    return 0

if __name__ == "__main__":
    # Note: These prints will go to output.txt if USE_FILE is True
    main()