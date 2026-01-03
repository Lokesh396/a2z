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

def sortedArray(a:List[int], b:List[int])->List:
    """
    
    Given two sorted arrays return the intersection of two arrays.

    Algorithm:
    - we use merge technique to store the elements present in both arrays.

    Args:
        a: input array 1 of integers
        b: input array 2 of integers

    Returns:
        Returns the output array
    
    Time Complexity: `O(min(m, n))`, given `m` and `n` is the length of `a` and `b` respectively.

    Space Complexity: `O(min(m,n))`, at max there will be that much elements.

    """
    m = len(a)
    n = len(b)

    i, j = 0, 0

    output = []

    while i < m and j < n:
        if a[i] < b[j]:
            i += 1
        elif a[i] > b[j]:
            j += 1
        else:
            output.append(a[i])       
            i += 1
            j += 1 

    
    return output
def main():
    # -------------------------
    # WRITE YOUR LOGIC BELOW
    # -------------------------
    
    arr1 = list(map(int, input().split()))
    arr2 = list(map(int, input().split()))
    print("Intersection: ", sortedArray(arr1, arr2))
    return 0

if __name__ == "__main__":
    # Note: These prints will go to output.txt if USE_FILE is True
    main()