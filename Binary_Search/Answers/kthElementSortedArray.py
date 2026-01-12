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

def kthElement( nums1: List[int], nums2: List[int], k) -> float:
    n1 = len(nums1)
    n2 = len(nums2)
    n = n1 + n2
    if n1 > n2:
        return kthElement(nums2, nums1, k)
    left = k

    low = max(k-n2, 0)
    high = min(k, n1)

    while low <= high:
        l1 , r1, l2, r2 = -float('inf'), float('inf'), -float('inf'), float('inf')
        
        mid1 = (low + high) // 2
        mid2 = left - mid1

        if mid1 < n1:
            r1 = nums1[mid1]
        if mid2 < n2:
            r2 = nums2[mid2]
        if mid1-1 >= 0: l1 = nums1[mid1-1]
        if mid2-1 >= 0: l2 = nums2[mid2-1]

        if l1 <= r2 and l2 <= r1:
            return max(l1, l2)
        
        elif l1 > r2:
            high = mid1 -1
        else:
            low = mid1 + 1
    return 0


def main():
    # -------------------------
    # WRITE YOUR LOGIC BELOW
    # -------------------------
    arr = list(map(int, input().split()))
    arr1 = list(map(int, input().split()))
    k = int(input())
    print('kth Element:',kthElement(arr, arr1, k))
    return 0

if __name__ == "__main__":
    # Note: These prints will go to output.txt if USE_FILE is True
    main()