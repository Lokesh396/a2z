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

def bubble_sort(n, arr):
    """
        Bubble sort works by the principle
        select the mazimum and place at the end 
        of array, by swaping adjacent elements.
    """
    for i in range(n-1, -1,-1):
        didSwap = False
        for j in range(i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                didSwap = True
        if(not didSwap):
            break
        print(arr, f"step -{n-i}")
    return arr
def main():
    # -------------------------
    # WRITE YOUR LOGIC BELOW
    # -------------------------
    n = int(input())
    arr = list(map(int, input().split()))
    print(arr, "unsorted")
    print(bubble_sort(n, arr=arr),"sorted")
    return 0

if __name__ == "__main__":
    # Note: These prints will go to output.txt if USE_FILE is True
    main()