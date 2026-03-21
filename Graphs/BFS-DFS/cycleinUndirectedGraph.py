import sys
import os
from pathlib import Path
from collections import defaultdict,deque

# Fast I/O and Recursion Setup
sys.setrecursionlimit(2000)
input = sys.stdin.readline

USE_FILE = True

if USE_FILE:
    BASE_DIR = Path(__file__).resolve().parents[2]
    sys.stdin = open(os.path.join(BASE_DIR, "input.txt"), "r")
    sys.stdout = open(os.path.join(BASE_DIR, "output.txt"), "w")


class Solution:
    def constructAdjList(self,edges):
        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        return adj
    
    def hasCycle(self, start, adj, vis):
        q = deque()
        q.append((start, -1))
        vis[start] = 1
        
        while q:
            cur, prev = q.popleft()
            for node in adj[cur]:
               if node != prev:
                    if vis[node] == 0:
                        q.append((node, cur))
                        vis[node] = 1
                    else:
                        return True
        
        return False
    
        
    def isCycle(self, V, edges):
        #Code here
        adj = self.constructAdjList(edges)
        vis = [0 for i in range(V)]
        
        for i in range(V):
            if vis[i] == 0:
                if self.hasCycle(i, adj, vis):
                    return True
        
        return False
    def isCycledfs(self, V, edges):
        adjList = defaultdict(list)
        for u, v in edges:
            adjList[u].append(v)
            adjList[v].append(u)
        
        def dfs(src, par, visited):
            if src in visited:
                return True
            visited.add(src)
            
            for nei in adjList[src]:
                if nei == par:
                    continue
                if dfs(nei, src, visited):
                    return True
            return False  # Outside the for loop
        
        visited = set()
        for i in range(V):  # Cover all vertices
            if i not in visited:
                if dfs(i, -1, visited):
                    return True
        return False

def main():
    # -------------------------
    # WRITE YOUR LOGIC BELOW
    # -------------------------
    sol = Solution()
    sol.isCycle(3,[[0,1],[1,0],[1,2]])
    return 0

if __name__ == "__main__":
    # Note: These prints will go to output.txt if USE_FILE is True
    main()