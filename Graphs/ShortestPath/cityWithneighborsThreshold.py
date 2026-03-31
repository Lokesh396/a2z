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

def findTheCity( n: int, edges: List[List[int]], distanceThreshold: int) -> int:
    
    dist = [[float('inf') for _ in range(n)] for _ in range(n)]

    for i in range(n):
        dist[i][i] = 0
    for u,v, w in edges:
        dist[u][v] = w      
        dist[v][u] = w
    for i in range(n):

        for j in range(n):
            for k in range(n):
                dist[j][k] = min(dist[j][k], dist[j][i] + dist[i][k]) 

    gcnt = n+1
    ans = 0
    for i in range(n):
        cnt = 0
        for j in range(n):
            if (i == j):
                continue
            if dist[i][j] <= distanceThreshold:
                cnt += 1
        if cnt <= gcnt:
            gcnt = cnt
            ans = i
    return ans


def main():
    # -------------------------
    # WRITE YOUR LOGIC BELOW
    # -------------------------
    
    return 0

if __name__ == "__main__":
    # Note: These prints will go to output.txt if USE_FILE is True
    main()