import sys
import os
from pathlib import Path
from collections import defaultdict, deque
from typing import List

# Fast I/O and Recursion Setup
sys.setrecursionlimit(2000)
input = sys.stdin.readline

USE_FILE = True

if USE_FILE:
    BASE_DIR = Path(__file__).resolve().parents[2]
    sys.stdin = open(os.path.join(BASE_DIR, "input.txt"), "r")
    sys.stdout = open(os.path.join(BASE_DIR, "output.txt"), "w")
    def shortestPath(self, V: int, E: int,
                     edges: List[List[int]]) -> List[int]:
        
        dis = [-1 for _ in range(V)]
        adjList = defaultdict(list)
        
        for u,v, w in edges:
            adjList[u].append((v, w))
        q = deque()
        q .append((0, 0))
        dis[0] = 0
        while q:
            nde, d = q.popleft()
            
            for child, cw in adjList[nde]:
                newdis = d + cw
                if dis[child] == -1 or newdis < dis[child]:
                    dis[child] = newdis
                    q.append((child, newdis))
        
        
        return dis

def main():
    # -------------------------
    # WRITE YOUR LOGIC BELOW
    # -------------------------
    
    return 0

if __name__ == "__main__":
    # Note: These prints will go to output.txt if USE_FILE is True
    main()