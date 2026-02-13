import sys
import os
from pathlib import Path
from typing import List
from collections import defaultdict

# Fast I/O and Recursion Setup
sys.setrecursionlimit(2000)
input = sys.stdin.readline

USE_FILE = True

if USE_FILE:
    BASE_DIR = Path(__file__).resolve().parents[2]
    sys.stdin = open(os.path.join(BASE_DIR, "input.txt"), "r")
    sys.stdout = open(os.path.join(BASE_DIR, "output.txt"), "w")

def atmost(nums, k):
        count = 0
        left = 0
        csum = 0
        for right in range(len(nums)):
            csum += nums[right]

            while csum > k and left <= right:
                csum -= nums[left]
                left += 1

            count += right - left + 1
        
        return count

def numSubarraysWithSum1( nums: List[int], goal: int) -> int:
    return atmost(nums, goal) - atmost(nums, goal-1)

def numSubarraysWithSum( nums: List[int], goal: int) -> int:
        seen = defaultdict(int)
        seen[0] = 1
        csum = 0
        count = 0
        for num in nums:
            csum += num
            diff = csum - goal
            if  diff in seen:
                count += seen[diff]
            seen[csum] += 1
        
        return count

def main():
    # -------------------------
    # WRITE YOUR LOGIC BELOW
    # -------------------------
    arr = list(map(int, input().split()))
    goal = int(input())
    print('no. of subarrays with sum:', numSubarraysWithSum(arr, goal))
    print('no. of subarrays with sum:', numSubarraysWithSum1(arr, goal))
    return 0

if __name__ == "__main__":
    # Note: These prints will go to output.txt if USE_FILE is True
    main()