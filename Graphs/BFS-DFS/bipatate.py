import sys
import os
from pathlib import Path
from typing import List
from collections import defaultdict

# Fast I/O and Recursion Setup
sys.setrecursionlimit(2000)
input = sys.stdin.readline

USE_FILE = True

if USE_FILE:
    BASE_DIR = Path(__file__).resolve().parents[2]
    sys.stdin = open(os.path.join(BASE_DIR, "input.txt"), "r")
    sys.stdout = open(os.path.join(BASE_DIR, "output.txt"), "w")

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        """
        Pattern: DFS / Graph 2-Coloring
        Difficulty: Medium
        Key Insight: Try to 2-color the graph — if any two adjacent nodes share the same color, it's not bipartite; handle disconnected components by iterating all nodes.
        Related: cycleinUndirectedGraph.py
        """
        adjList = defaultdict(list)
        for idx, val in enumerate(graph):
            adjList[idx] = val
        

        visited = [-1 for i in range(len(graph))]

        def dfs(i, c):
            visited[i] = c

            for child in adjList[i]:
                nc = 1 if c == 0 else 0
                if visited[child] != -1:
                    if visited[child] == c:
                        return False
                else:
                    if not dfs(child, nc):
                        return False
            
            return True

        for i in range(len(graph)):
            if visited[i] == -1:
                if not dfs(i, 0):
                    return False
    
        return True
            

def main():
    # -------------------------
    # WRITE YOUR LOGIC BELOW
    # -------------------------
    
    return 0

if __name__ == "__main__":
    # Note: These prints will go to output.txt if USE_FILE is True
    main()