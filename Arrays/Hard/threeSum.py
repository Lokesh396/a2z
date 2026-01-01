import sys
import os
from pathlib import Path
from typing import *
# Fast I/O and Recursion Setup
sys.setrecursionlimit(2000)
input = sys.stdin.readline

USE_FILE = True

if USE_FILE:
    BASE_DIR = Path(__file__).resolve().parents[2]
    sys.stdin = open(os.path.join(BASE_DIR, "input.txt"), "r")
    sys.stdout = open(os.path.join(BASE_DIR, "output.txt"), "w")

def threeSumBetter( nums: List[int]) -> List[List[int]]:
        
    ans = set()
    for i in range(len(nums)):
        hashmap = set()
        for j in range(i+1,len(nums)):
            tempsum = -(nums[i]+nums[j])
            if tempsum in hashmap:
                temp = [nums[i], tempsum,nums[j]]
                temp.sort()
                ans.add(tuple(temp))
            hashmap.add(nums[j])
    
    return list(ans)

def threeSumOptimal( nums: List[int]) -> List[List[int]]:
    nums.sort()
    n =  len(nums)
    ans = []
    for i in range(n-2):
        if i > 0 and nums[i] == nums[i-1]:
            continue
        j = i+ 1
        k = n - 1
        while j <  k:
            tsum = nums[i] + nums[j] + nums[k]
            if tsum == 0:
                ans.append([nums[i], nums[j], nums[k]])
                j += 1
                while j < k and nums[j] == nums[j-1]:
                    j += 1
                k -= 1
                while k >j and nums[k] == nums[k+1]:
                    k -= 1
            elif tsum < 0:
                j += 1
            else:
                k -= 1
    return ans
def main():
    # -------------------------
    # WRITE YOUR LOGIC BELOW
    # -------------------------
    arr = list(map(int, input().split()))
    print('Unique triplets: ', threeSumBetter(arr))
    print('Unique triplets: ',threeSumOptimal(arr))
    return 0

if __name__ == "__main__":
    # Note: These prints will go to output.txt if USE_FILE is True
    main()