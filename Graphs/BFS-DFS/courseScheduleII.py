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

def findOrder(numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        visited = [0 for _ in range(numCourses)]
        path = [0 for _ in range(numCourses)]
        out =  []

        adjList = defaultdict(list)
        for v, u in prerequisites:
            adjList[u].append(v)

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
            out.append(node)
            path[node] = 0
            return False


        for i in range(numCourses):
            if dfs(i):
                return []

        return out[::-1]

def main():
    # -------------------------
    # WRITE YOUR LOGIC BELOW
    # -------------------------
    
    return 0

if __name__ == "__main__":
    # Note: These prints will go to output.txt if USE_FILE is True
    main()