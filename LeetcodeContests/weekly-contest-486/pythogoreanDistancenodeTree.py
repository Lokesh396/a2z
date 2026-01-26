from collections import defaultdict, deque
from typing import List

class Solution:
    def adjacencyList(self,edges):
        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        return adj
    def getallDistances(self,adj,start,target):
        
        visited = set()
        queue = deque()
        queue.append([start,0])
        visited.add(start)
        while queue:
            curr,d = queue.popleft()
            if curr == target:
                return d
            for child in adj[curr]:
                if child not in visited:
                    queue.append([child,d+1])
                    visited.add(child)
                    
    def bfs(self,adj,start,n):
        d = [-1 for i in range(n)]
        q = deque()
        q.append(start)
        d[start] = 0
        while q:
            node = q.popleft()

            for nei in adj[node]:
                if d[nei] == -1:
                    d[nei] = d[node] + 1
                    q.append(nei)
        return d
        
    def specialNodes(self, n: int, edges: List[List[int]], x: int, y: int, z: int) -> int:
        adj = self.adjacencyList(edges)
        outcnt = 0
        dx = self.bfs(adj, x, n)
        dy = self.bfs(adj, y, n)
        dz = self.bfs(adj, z, n)
        for key, value in adj.items():
            out = [dx[key],dy[key],dz[key]]
            if -1 in out:
                continue
            out.sort()
            if out[0]** 2 + out[1]**2 == out[2]**2:
                outcnt += 1

        return outcnt
         