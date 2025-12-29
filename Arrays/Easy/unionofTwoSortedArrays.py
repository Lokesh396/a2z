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

def appendValue(output, val):
    if len(output) == 0 or  output[-1] != val:
        output.append(val)
def sortedArray(a, b):
    # Write your code here
    m = len(a)
    n = len(b)

    i, j = 0, 0

    output = []

    while i < m and j < n:
        val = 0
        if a[i] < b[j]:
            val = a[i]
            i += 1
        else:
            val = b[j]
            j += 1
        appendValue(output, val)        

    
    while i < m:
       appendValue(output, a[i])
       i += 1

    
    while j < n:
        appendValue(output, b[j])
        j += 1

    
    return output
def main():
    # -------------------------
    # WRITE YOUR LOGIC BELOW
    # -------------------------
    arr1 = list(map(int, input().split()))
    arr2 = list(map(int, input().split()))
    print("Union", sortedArray(arr1, arr2))
    return 0

if __name__ == "__main__":
    # Note: These prints will go to output.txt if USE_FILE is True
    main()