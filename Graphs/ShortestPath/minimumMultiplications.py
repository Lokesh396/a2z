import sys
import os
from pathlib import Path
import heapq
from typing import List

# Fast I/O and Recursion Setup
sys.setrecursionlimit(2000)
input = sys.stdin.readline

USE_FILE = True

if USE_FILE:
    BASE_DIR = Path(__file__).resolve().parents[2]
    sys.stdin = open(os.path.join(BASE_DIR, "input.txt"), "r")
    sys.stdout = open(os.path.join(BASE_DIR, "output.txt"), "w")
#User function Template for python3

 
class Solution:
    
    def minimumMultiplications(self, arr : List[int], start : int, end : int) -> int:
        # code here
        
        if start == end:
            return 0
        
        q = [[0,start]]
        dist = [float('inf') for i in range(100000)]
        
        while q:
            
            dis, node = heapq.heappop(q)
            
            for child in arr:
                newdis = dis + 1
                newsrc = (child * node) % 100000
                
                if dist[newsrc] > newdis:
                    dist[newsrc] = newdis
                    heapq.heappush(q, [newdis, newsrc])
        
        return dist[end] if dist[end] != float('inf') else -1
def main():
    # -------------------------
    # WRITE YOUR LOGIC BELOW
    # -------------------------
    
    return 0

if __name__ == "__main__":
    # Note: These prints will go to output.txt if USE_FILE is True
    main()