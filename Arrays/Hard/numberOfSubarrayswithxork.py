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

def subarrays(nums, k):

    prexor = 0
    prexormap = {0:1}
    count = 0
    for num in nums:
        prexor = prexor ^ num

        diff = prexor ^ k
        count += prexormap.get(diff, 0)

        prexormap[prexor] = prexormap.get(prexor, 0) + 1
    
    return count

def main():
    # -------------------------
    # WRITE YOUR LOGIC BELOW
    # -------------------------
    
    arr = list(map(int, input().split()))
    k = int(input())
    print('Subarrays with xor k:', subarrays(arr, k))
    return 0

if __name__ == "__main__":
    # Note: These prints will go to output.txt if USE_FILE is True
    main()