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

def removeStones( stones: List[List[int]]) -> int:
    
    rows = 0
    cols = 0
    for u,v in stones:
        rows = max(rows, u+1)
        cols = max(cols,v+1)
    
    parent =[i for i in range(rows+cols)]
    rank = [0 for i in range(rows+cols)]

    def findulp(node):
        if parent[node] == node:
            return node
        parent[node] = findulp(parent[node])
        return parent[node]
    
    def unionbyrank(u,v):
        up_u = findulp(u)
        up_v = findulp(v)

        if rank[up_u] < rank[up_v]:
            parent[up_u] = up_v
        elif rank[up_v] < rank[up_u]:
            parent[up_v] = up_u
        else:
            parent[up_v] = up_u
            rank[up_u] += 1
    
    for u, v in stones:
        unionbyrank(u, v+rows)
    components = set()

    # Count number of connected components
    for x, y in stones:
        components.add(findulp(x))
    return len(stones) - len(components)
def main():
    # -------------------------
    # WRITE YOUR LOGIC BELOW
    # -------------------------
    
    return 0

if __name__ == "__main__":
    # Note: These prints will go to output.txt if USE_FILE is True
    main()