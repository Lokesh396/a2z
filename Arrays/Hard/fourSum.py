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
def fourSum( nums: List[int], target: int) -> List[List[int]]:
    n = len(nums)

    nums.sort()
    ans = list()
    for i in range(n):
        if i > 0 and nums[i] == nums[i-1]:
            continue
        for j in range(i+1, n):
            if j> i+1 and  nums[j] == nums[j-1]:
                continue

            k = j+1
            l = n-1

            while k < l:
                tsum = nums[i] + nums[j] + nums[k] + nums[l]
                if tsum == target:
                    ans.append([nums[i], nums[j], nums[k], nums[l]])
                    k += 1
                    l -= 1
                    while k < l and nums[k] == nums[k-1]: k += 1
                    while k < l and nums[l] == nums[l+1]: l -= 1
                elif tsum < target:
                    k += 1
                else:
                    l -= 1
    
    return ans
def main():
    # -------------------------
    # WRITE YOUR LOGIC BELOW
    # -------------------------
    arr = list(map(int, input().split()))
    target = int(input())
    print('unique Quadraplets:', fourSum(arr, target))
    return 0

if __name__ == "__main__":
    # Note: These prints will go to output.txt if USE_FILE is True
    main()