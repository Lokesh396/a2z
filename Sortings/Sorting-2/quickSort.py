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


def partition(arr, low, high):
    i = low
    j = high
    while i < j:
        
        while i <= high and arr[i] <= arr[low]:
            i += 1
        
        while j >= low and arr[j] > arr[low]:
            j -= 1
        
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
    arr[low], arr[j] = arr[j],arr[low]
    return j

def quick_sort(arr, low, high):
    if low < high:
        pElement = arr[low]
        pIndex = partition(arr, low, high)
        print(low, high, pIndex, pElement, arr)
        quick_sort(arr, low, pIndex-1)
        quick_sort(arr, pIndex+1, high)
def main():
    # -------------------------
    # WRITE YOUR LOGIC BELOW
    # -------------------------
    n = int(input())
    arr = list(map(int, input().split()))
    print(arr, 'unsorted')
    quick_sort(arr,0,n-1)
    print(arr, 'sorted')
    return 0

if __name__ == "__main__":
    # Note: These prints will go to output.txt if USE_FILE is True
    main()