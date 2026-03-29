import sys
import os
from pathlib import Path
from collections import defaultdict
from typing import List
import heapq

# Fast I/O and Recursion Setup
sys.setrecursionlimit(2000)
input = sys.stdin.readline

USE_FILE = True

if USE_FILE:
    BASE_DIR = Path(__file__).resolve().parents[2]
    sys.stdin = open(os.path.join(BASE_DIR, "input.txt"), "r")
    sys.stdout = open(os.path.join(BASE_DIR, "output.txt"), "w")

def countPaths(n: int, roads: List[List[int]]) -> int:
    
    dist = [float('inf') for _ in range(n)]
    ways = [0 for _ in range(n)]
    adjList = defaultdict(list)

    for u, v, w in roads:
        adjList[u].append((v, w))
        adjList[v].append((u, w))

    q = []
    heapq.heappush(q, [0, 0])
    dist[0] = 0
    ways[0] = 1
    while q:
        dis, node = heapq.heappop(q)

        for child, w in adjList[node]:
            newdis = dis + w
            if newdis < dist[child]:
                dist[child] = newdis
                ways[child] = ways[node]
                heapq.heappush(q, [newdis, child])
            elif newdis == dist[child]:
                ways[child] += ways[node]
    return ways[-1] % 1000000007
        
def main():
    # -------------------------
    # WRITE YOUR LOGIC BELOW
    # -------------------------
    
    return 0

if __name__ == "__main__":
    # Note: These prints will go to output.txt if USE_FILE is True
    main()