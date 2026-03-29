import sys
import os
from pathlib import Path
from collections import deque, defaultdict
from typing import List

# Fast I/O and Recursion Setup
sys.setrecursionlimit(2000)
input = sys.stdin.readline

USE_FILE = True

if USE_FILE:
    BASE_DIR = Path(__file__).resolve().parents[2]
    sys.stdin = open(os.path.join(BASE_DIR, "input.txt"), "r")
    sys.stdout = open(os.path.join(BASE_DIR, "output.txt"), "w")

def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
    
    dist = [-1 for _ in range(n+1)]
    adjList = defaultdict(list)

    for u, v, w in times:
        adjList[u].append((v, w))
    

    q = deque()
    q.append([k, 0])
    dist[k] = 0
    while q:
        node, dis = q.popleft()

        if dis > dist[node]:
            continue

        for child, w in adjList[node]:
            newdis = dis + w
            if dist[child] == -1 or  newdis < dist[child]:
                dist[child] = newdis
                q.append([child, newdis])
    
    ans = -1
    for i in range(1, n+1):
        if k != i:
            if dist[i] == -1:
                return -1
            ans = max(dist[i], ans)
    
    return ans
def main():
    # -------------------------
    # WRITE YOUR LOGIC BELOW
    # -------------------------
    
    return 0

if __name__ == "__main__":
    # Note: These prints will go to output.txt if USE_FILE is True
    main()