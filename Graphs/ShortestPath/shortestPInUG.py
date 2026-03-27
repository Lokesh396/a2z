import sys
import os
from pathlib import Path
from collections import defaultdict, deque

# Fast I/O and Recursion Setup
sys.setrecursionlimit(2000)
input = sys.stdin.readline

USE_FILE = True

if USE_FILE:
    BASE_DIR = Path(__file__).resolve().parents[2]
    sys.stdin = open(os.path.join(BASE_DIR, "input.txt"), "r")
    sys.stdout = open(os.path.join(BASE_DIR, "output.txt"), "w")

def shortestPath(V, edges, src):
    # code here
    dis = [-1 for _ in range(V)]
    
    adjList = defaultdict(list)
    
    for u,v in edges:
        adjList[u].append(v)
        adjList[v].append(u)
    
    q = deque()
    q.append((src, 0))
    dis[src] = 0
    
    while q:
        node, dist = q.popleft()
        
        for child in adjList[node]:
            newdis = dist + 1
            if dis[child] == -1 or  newdis < dis[child]:
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