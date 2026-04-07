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

# Memoization  
def frogJumpMemo(n: int, heights: List[int]) -> int:

    # Write your code here.
    dp = [0] * (n+1)
    def jump(c):
        if c == 0:
            return 0
        if dp[c]:
            return dp[c]
        l = jump(c-1) + abs(heights[c] - heights[c-1])
        r = float('inf')
        if c > 1:
            r = jump(c-2)+ abs(heights[c] - heights[c-2])
        
        dp[c] = min(l,r)
        return dp[c]

    return jump(n-1)

# Tabluation

def frogJumpTabu(n: int, heights: List[int]) -> int:
    if n == 1:
        return 0
    # Write your code here.
    memory = [0 for i in range(n)]

    memory[0] = 0
    memory[1] = abs(heights[0]-heights[1])
    for i in range(2, n):
        memory[i] = min(abs(heights[i]-heights[i-1]) + memory[i-1] , abs(heights[i]-heights[i-2]) + memory[i-2])
    return memory[n-1]

# Space Optimization

def frogJump(n:int, heights: List[int]) -> int:
    if n == 1:
        return 0
    
    prev = 0
    curr = abs(heights[0]-heights[1])

    for i in range(2, n):
        temp = curr
        curr =  min(abs(heights[i]-heights[i-1]) +  curr, abs(heights[i]-heights[i-2]) + prev)
        prev = temp
    
    return curr

def main():
    # -------------------------
    # WRITE YOUR LOGIC BELOW
    # -------------------------
    
    return 0

if __name__ == "__main__":
    # Note: These prints will go to output.txt if USE_FILE is True
    main()