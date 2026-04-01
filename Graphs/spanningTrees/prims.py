import sys
import os
from pathlib import Path
from collections import defaultdict
import heapq

# Fast I/O and Recursion Setup
sys.setrecursionlimit(2000)
input = sys.stdin.readline

USE_FILE = True

if USE_FILE:
    BASE_DIR = Path(__file__).resolve().parents[2]
    sys.stdin = open(os.path.join(BASE_DIR, "input.txt"), "r")
    sys.stdout = open(os.path.join(BASE_DIR, "output.txt"), "w")
def spanningTree(self, V, edges):
    # code here
    
    
    visited = [0 for i in range(V)]
    
    adjList = defaultdict(list)
    for u,v,w in edges:
        adjList[u].append([v, w])
        adjList[v].append([u, w])
        
    
    
    pq = [[0,0,-1]]
    s = 0
    mst = []
    while pq:
        
        w, n, p = heapq.heappop(pq)
        
        if visited[n] == 0 and p != -1:
            mst.append([p, n, w])
            s += w
        visited[n] = 1
        
        for child, w in adjList[n]:
            if visited[child] == 0:
                heapq.heappush(pq, [w, child, n])
    
    return s
def main():
    # -------------------------
    # WRITE YOUR LOGIC BELOW
    # -------------------------
    
    return 0

if __name__ == "__main__":
    # Note: These prints will go to output.txt if USE_FILE is True
    main()