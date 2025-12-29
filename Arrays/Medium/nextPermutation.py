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
def nextPermutation(nums):

    n = len(nums)
    ind = -1
    for i in range(n-2, -1, -1):
        if nums[i] < nums[i+1]:
            ind = i
            break
    if ind == -1:
        nums.reverse()
        return
    
    for i in range(n-1, ind, -1):
        if nums[i] > nums[ind]:
            nums[i], nums[ind] = nums[ind], nums[i]
            break
    ind += 1
    while ind < n-1:
        nums[ind], nums[n-1] = nums[n-1], nums[ind]
        ind += 1
        n -= 1
        
def main():
    # -------------------------
    # WRITE YOUR LOGIC BELOW
    # -------------------------
    arr = list(map(int, input().split()))
    nextPermutation(arr)
    print('Next Permuatation: ', *arr)
    return 0

if __name__ == "__main__":
    # Note: These prints will go to output.txt if USE_FILE is True
    main()