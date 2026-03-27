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
    # Returns shortest distances from src to all other vertices

def dijkstra(V, edges, src):
    # code here
    
    dist = [-1 for _ in range(V)]
    dist[src] = 0
    adjList = defaultdict(list)
    for u,v,w in edges:
        adjList[u].append([v, w])
        adjList[v].append([u, w])
    heap = []
    heapq.heappush(heap, [0, src])
    while heap:
        
        d, node = heapq.heappop(heap)
        if d > dist[node]:
            continue
        for child, w in adjList[node]:
            newdis = d+ w
            if dist[child] == -1 or newdis < dist[child]:
                dist[child] = newdis
                heapq.heappush(heap, [newdis, child])
    
    return dist
def main():
    # -------------------------
    # WRITE YOUR LOGIC BELOW
    # -------------------------
    
    return 0

if __name__ == "__main__":
    # Note: These prints will go to output.txt if USE_FILE is True
    main()