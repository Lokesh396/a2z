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
def rearrangeArray(nums):
    pos = 0
    neg = 1
    out = [0 for i in range(len(nums))]
    for num in nums:
        if num < 0:
            out[neg] = num
            neg += 2
        else:
            out[pos] = num
            pos += 2
    
    return out

def version2(nums):
    positives = []
    negatives = []
    for num in nums:
        if num < 0:
            negatives.append(num)
        else:
            positives.append(num)
    if len(positives) > len(negatives):
        for i in range(len(negatives)):
            nums[i*2] = positives[i]
            nums[i*2+1] = negatives[i]
        ind = len(negatives) * 2
        for i in range(len(negatives), len(positives)):
            nums[ind] = positives[i]
            ind += 1

    else:
        for i in range(len(positives)):
            nums[i*2] = positives[i]
            nums[i*2+1] = positives[i]
        ind = len(positives) * 2
        for i in range(len(positives), len(negatives)):
            nums[ind] = positives[i]
            ind += 1
    return nums
def main():
    # -------------------------
    # WRITE YOUR LOGIC BELOW
    # -------------------------
    arr = list(map(int, input().split()))
    arr1 = list(map(int, input().split()))
    print('Rearranged Array v1: ', rearrangeArray(arr))
    print('Rearranged Array v2: ',version2(arr1))
    return 0

if __name__ == "__main__":
    # Note: These prints will go to output.txt if USE_FILE is True
    main()