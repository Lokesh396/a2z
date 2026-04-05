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
class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        
        if len(connections) < n - 1:
            return - 1
        

        rank = [0 for _ in range(n+1)]
        parent = [i for i in range(n+1)]

        def findulp(node):
            if parent[node] == node:
                return node
            
            parent[node] = findulp(parent[node])
            return parent[node]
        def unionByrank(u, v):
            ul_u = findulp(u)
            ul_v = findulp(v)

            if rank[ul_u] < rank[ul_v]:
                parent[ul_u] = ul_v
            elif rank[ul_v] < rank[ul_u]:
                parent[ul_v] = ul_u
            else:
                parent[ul_v] = ul_u
                rank[ul_u] += 1
        for u, v in connections:
            unionByrank(u, v)
        cnt = 0
        for i in range(n):
            if findulp(0) != findulp(i):
                cnt += 1
                unionByrank(0, i)
        
        return cnt
def main():
    # -------------------------
    # WRITE YOUR LOGIC BELOW
    # -------------------------
    
    return 0

if __name__ == "__main__":
    # Note: These prints will go to output.txt if USE_FILE is True
    main()