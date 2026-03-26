import sys
import os
from pathlib import Path
from collections import defaultdict
from typing import List

# Fast I/O and Recursion Setup
sys.setrecursionlimit(2000)
input = sys.stdin.readline

USE_FILE = True

if USE_FILE:
    BASE_DIR = Path(__file__).resolve().parents[2]
    sys.stdin = open(os.path.join(BASE_DIR, "input.txt"), "r")
    sys.stdout = open(os.path.join(BASE_DIR, "output.txt"), "w")
def eventualSafeNodes(graph: List[List[int]]) -> List[int]:
        """
        Pattern: DFS / Cycle Detection (Safe Node Identification)
        Difficulty: Medium
        Key Insight: A node is safe iff it is not part of a cycle and all its paths eventually terminate — reuse DFS path-tracking: safe = not in any cycle path.
        Related: courseScheduleII.py, cycleinDG.py
        """
        v = len(graph)
        visited = [0 for _ in range(v)]
        path = [0 for _ in range(v)]
        out =  []

        adjList = defaultdict(list)
        for idx in range(v):
            adjList[idx] = graph[idx]

        def dfs(node):
            if path[node] != 0:
                return True
            if visited[node] != 0:
                return False

            path[node] = 1
            visited[node] = 1

            for child in adjList[node]:
                if dfs(child):
                    return True
            path[node] = 0
            return False


        for i in range(v):
            if not dfs(i):
                out.append(i)

        return out

def main():
    # -------------------------
    # WRITE YOUR LOGIC BELOW
    # -------------------------
    
    return 0

if __name__ == "__main__":
    # Note: These prints will go to output.txt if USE_FILE is True
    main()