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
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1

def rotate_array(arr, n ,k):
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