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


def nextGreaterElement( nums1: List[int], nums2: List[int]) -> List[int]:
        
    stack = []

    memory = dict()

    for i in range(len(nums2)-1, -1, -1):

        while stack and stack[-1] < nums2[i]:
            stack.pop()
        
        if stack:
            memory[nums2[i]] = stack[-1]
        else:
            memory[nums2[i]] = -1
        
        stack.append(nums2[i])
    
    ans = []

    for num in nums1:
        ans.append(memory.get(num, -1))
    
    return ans

def main():
    # -------------------------
    # WRITE YOUR LOGIC BELOW
    # -------------------------
    arr = list(map(int, input().split()))
    arr1 = list(map(int, input().split()))
    print('next Greater element:',nextGreaterElement(arr, arr1))
    return 0

if __name__ == "__main__":
    # Note: These prints will go to output.txt if USE_FILE is True
    main()