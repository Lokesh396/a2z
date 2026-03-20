import sys
import os
from pathlib import Path
from collections import defaultdict
from typing import Optional, List

# Fast I/O and Recursion Setup
sys.setrecursionlimit(2000)
input = sys.stdin.readline

USE_FILE = True

if USE_FILE:
    BASE_DIR = Path(__file__).resolve().parents[2]
    sys.stdin = open(os.path.join(BASE_DIR, "input.txt"), "r")
    sys.stdout = open(os.path.join(BASE_DIR, "output.txt"), "w")
class Solution:
    def constructAdjList(self,arr, m):
        adj = defaultdict(list)
        for i in range(m):
            for j in range(m):
                if i != j and arr[i][j] == 1:
                    adj[i].append(j)
                    adj[j].append(i)
        return adj
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        m = len(isConnected)
        adj = self.constructAdjList(isConnected, m)

        def dfs(i):
            if visited[i] == 0:
                visited[i] = 1
            
            for j in (adj[i]):
                if visited[j] == 0:
                    dfs(j)

        visited = [0 for _ in range(m)]

        cnt = 0
        for i in range(m):
            if visited[i] == 0:
                dfs(i)
                cnt += 1
        
        return cnt
def main():
    # -------------------------
    # WRITE YOUR LOGIC BELOW
    # -------------------------
    
    return 0

if __name__ == "__main__":
    # Note: These prints will go to output.txt if USE_FILE is True
    main()