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


def reverse(start, end, arr):
    """
    Reverse an array in place
    
    Args:
        start: start index
        end: end index
        arr: array that needs to be reverse
    """
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1

def rotate_array(arr, n ,k):
    """
    
    Rotate an array by k places either left or right

    Algorithm:
    - To rotate right, take k = n - k
    - reverse the elements from 0 to k
    - reverse the elements from k to n-1
    - reverse the whole array
    
    Args:
        arr: input array
        n: length of the array
        k: no of places to rotate
    
    Returns:
        Rotates the array in place.
    
    Time Complexity : O(n) reversing the arrays
    Space Complexity: O(1) we didn't take any extra space

    """
    k = k % n

    # for rotaing right uncomment this
    # k = n - k 
    reverse(0, k-1, arr)
    reverse(k, n-1, arr)
    reverse(0, n-1, arr)
    

def main():
    # -------------------------
    # WRITE YOUR LOGIC BELOW
    # -------------------------
    n = int(input())
    k = int(input())
    arr = list(map(int, input().split()))
    print(arr, f"Before {k} Rotations")
    rotate_array(arr, n , k)
    print(arr, f"After {k} Rotations")
    return 0

if __name__ == "__main__":
    # Note: These prints will go to output.txt if USE_FILE is True
    main()