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
def maxSubArray( nums):
    csum = 0
    arrStart , arrEnd = -1 , -1
    start = 0
    gmax = -float('inf')
    for i in range(len(nums)):

        csum += nums[i]

        if csum > gmax:
            gmax = csum
            arrStart = start
            arrEnd = i

        if csum < 0:
            csum = 0
            start = i

    
    return [arrStart, arrEnd]
def main():
    # -------------------------
    # WRITE YOUR LOGIC BELOW
    # -------------------------
    arr = list(map(int, input().split()))
    print('Maximum Subarray sum locates at : ',maxSubArray(arr) )
    return 0

if __name__ == "__main__":
    # Note: These prints will go to output.txt if USE_FILE is True
    main()