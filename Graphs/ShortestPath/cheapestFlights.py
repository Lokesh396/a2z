import sys
import os
from pathlib import Path
import heapq
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
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adjList = defaultdict(list)
        for u,v,price in flights:
            adjList[u].append((v, price))
        dis = [[float('inf') for i in range(k+2)] for _ in range(n+1)]
        dis[src][0] = 0
        q = []
        heapq.heappush(q, [0,src, 0])
        while q:

            price, node, stops = heapq.heappop(q)
            if node == dst:
                return price
            if stops == k+1:
                continue            

            for child, pri in adjList[node]:
                newpri = price + pri
                if newpri < dis[child][stops+1]:
                    dis[child][stops+1] = newpri
                    heapq.heappush(q, [price+pri, child, stops+1])
        
        return -1
def main():
    # -------------------------
    # WRITE YOUR LOGIC BELOW
    # -------------------------
    
    return 0

if __name__ == "__main__":
    # Note: These prints will go to output.txt if USE_FILE is True
    main()