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
count = [0]
def merge(arr, p, q, r):
    left = p
    right = q+1
    tarr = [0 for i in range(r-p+1)]
    idx =0

    while left <= q and right <= r:
        if arr[left] > arr[right]:
            print(arr[left:q+1], arr[right])
            count[0] += (q-left) + 1
            tarr[idx] = arr[right]
            right += 1
        else:
            tarr[idx] = arr[left]
            left += 1
        
        idx += 1
    
    while left <= q:
        tarr[idx] = arr[left]
        left += 1
        idx += 1
    while right <= r:
        tarr[idx] = arr[right]
        right += 1
        idx += 1
    
    arr[p:r+1] = tarr[::]
def merge_sort(arr, p, r):
    """
    Counts inversions in `arr` using merge sort partitioning.

    An inversion is a pair (i, j) where i < j and arr[i] > arr[j]. We split the
    array, recursively count inversions in each half, then count cross-half
    inversions during merge when a right element is placed before remaining
    left elements.

    Args:
        arr: List of integers.
        p: Start index (inclusive).
        r: End index (inclusive).

    Returns:
        None; updates the global `count` list in-place with total inversions.

    Time Complexity: O(n log n)
    Space Complexity: O(n) for the temporary array in merge.
    """
    if p < r:
        q = (p+r) // 2
        merge_sort(arr, p, q)
        merge_sort(arr, q+1,r)
        merge(arr,p, q, r)

def main():
    # -------------------------
    # WRITE YOUR LOGIC BELOW
    # -------------------------
    arr = list(map(int, input().split()))
    merge_sort(arr, 0, len(arr)-1)
    print('Inversions count:',count[0])

if __name__ == "__main__":
    # Note: These prints will go to output.txt if USE_FILE is True
    main()
