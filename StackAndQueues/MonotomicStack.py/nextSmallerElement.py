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

def nextSmallerElement(arr,n):
    # Write your code here.
    stack = []
    ans = [-1 for i in range(n)]

    for i in range(n-1, -1, -1):

        num = arr[i]
        while stack and stack[-1] >= num:
            stack.pop()
        
        if stack:
            ans[i] = stack[-1]
        
        stack.append(num)
    
    return ans

def main():
    # -------------------------
    # WRITE YOUR LOGIC BELOW
    # -------------------------
    arr = list(map(int, input().split()))
    print('nextSmallerElement:', nextSmallerElement(arr, len(arr)))
    return 0

if __name__ == "__main__":
    # Note: These prints will go to output.txt if USE_FILE is True
    main()