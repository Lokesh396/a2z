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
def bellmanFord( V, edges, src):
    #code here
    
    dist = [float('inf') for _ in range(V)]
    
    dist[src] = 0
    
    for i in range(V-1):
        for u,v,w in edges:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
    
    for u,v,w in edges:
        if dist[u] + w < dist[v]:
            return [-1]
    
    for i in range(V):
        if dist[i] == float('inf'):
            dist[i] = 10**8
    
    return dist
def main():
    # -------------------------
    # WRITE YOUR LOGIC BELOW
    # -------------------------
    
    return 0

if __name__ == "__main__":
    # Note: These prints will go to output.txt if USE_FILE is True
    main()