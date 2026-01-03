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
def merge(arr, p, q, r):
    left = p
    right = q+1
    tarr = [0 for i in range(r-p+1)]
    idx =0
    count = 0
    while left <= q and right <= r:
        if arr[left] > 2* arr[right]:
            print(arr[left:q+1], arr[right])
            count += (q-left)+1
            right += 1
        else:
            left += 1
    left = p
    right = q+1
    while left <= q and right <= r:
        if arr[left] > arr[right]:
           
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
    return count
def merge_sort(arr, p, r):
    count = 0
    if p < r:
        q = (p+r) // 2
        count += merge_sort(arr, p, q)
        count += merge_sort(arr, q+1,r)
        count += merge(arr,p, q, r)
    return count

def main():
    # -------------------------
    # WRITE YOUR LOGIC BELOW
    # -------------------------
    arr = list(map(int, input().split()))
    
    print('Inversions count:',merge_sort(arr, 0, len(arr)-1))

if __name__ == "__main__":
    # Note: These prints will go to output.txt if USE_FILE is True
    main()