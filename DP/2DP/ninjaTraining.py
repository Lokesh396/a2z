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

def ninjaTraining(n: int, points: List[List[int]]) -> int:

    # Write your code here.

    dp = [[-1 for i in range(4)] for _ in range(n)]
    def dfs(day, last):
        if day < 0:
            return 0
        if dp[day][last] != -1:
            return dp[day][last]
        maxi = -float('inf')
        for i in range(3):
            if last != i:
                point = points[day][i] + dfs(day-1, i)
                maxi = max(maxi, point)
        dp[day][last] = maxi
        return maxi
    
    return dfs(n-1, 3)

def ninjaTraining(n: int, points: List[List[int]]) -> int:
    prev = [0 for i in range(4)]

    prev[0] = max(points[0][1],points[0][2])
    prev[1] = max(points[0][0],points[0][2])
    prev[2] = max(points[0][1],points[0][0])
    prev[3] = max(points[0][1],points[0][2], points[0][1])

    for i in range(1,n):
        temp = [0] * 4
        for last in range(4):
            for task in range(3):
                if last != task:
                    temp[last] = max(temp[last] , points[i][task] + prev[task]) 
        prev = temp
    return prev[3]

def main():
    # -------------------------
    # WRITE YOUR LOGIC BELOW
    # -------------------------
    
    return 0

if __name__ == "__main__":
    # Note: These prints will go to output.txt if USE_FILE is True
    main()