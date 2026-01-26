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
def lower_bound( nums, n, t):
    """
    You are given an array 'arr' sorted in non-decreasing order and a number 'x'. 
    You must return the index of the lower bound of 'x'.

    Algorithm:
    - Do a straight forward binary search here we have only two cases
        - greater than or equal to 
        - else less than

    Args:
        arr: sorted input array
        n: length of the array
        x: target element
    
    Returns: returns the index of the lower bound of x.

    Time Complexity: O(lgn)

    Space Complexity: O(1)
    """
    low = 0
    high = n-1
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] >= t:
            high = mid - 1
        else:
            low = mid + 1
    return low
    
def rowMaxOnes(mat, n, m):
    """
    We will iterate through each row and find the row with the highest no of 1s.

    Time Complexity: O(nlgm)

    Space Complexity: O(1)
    """
    cnt = 0
    idx = -1
    for i in range(n):
        ones = m - lower_bound(mat[i], m, 1)
        if ones > cnt:
            cnt = ones
            idx = i
    
    return idx
def main():
    # -------------------------
    # WRITE YOUR LOGIC BELOW
    # -------------------------
    n = int(input())
    mat = []
    for i in range(n):
        arr=list(map(int, input().split()))
        mat.append(arr)
    
    print('Row with max ones:', rowMaxOnes(mat, n, len(mat[0])))
    return 0

if __name__ == "__main__":
    # Note: These prints will go to output.txt if USE_FILE is True
    main()