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
    """
    Given an array return count of subarray  whose xor is k

    Algorithm:
    - we will store the xor of all the elements and store them in hashmap.
    - It is similar to the problem subarrays with sum k.

    Args:
    nums: input array
    k: xor value

    Returns: return the count of subarrays with xor as k.

    Time Complexity: O(n)

    Space Complexity: O(n)
    """

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