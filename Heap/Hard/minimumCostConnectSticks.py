import sys
import os
from pathlib import Path
import heapq

# Fast I/O and Recursion Setup
sys.setrecursionlimit(2000)
input = sys.stdin.readline

USE_FILE = True

if USE_FILE:
    BASE_DIR = Path(__file__).resolve().parents[2]
    sys.stdin = open(os.path.join(BASE_DIR, "input.txt"), "r")
    sys.stdout = open(os.path.join(BASE_DIR, "output.txt"), "w")
def minimumCostToConnectSticks(arr):
    # Write your code here.
    
    heapq.heapify(arr)
    cost = 0
    while len(arr) >= 2:
        ele1 = heapq.heappop(arr)
        ele2 = heapq.heappop(arr)
        cost += ele1 + ele2
        heapq.heappush(arr, ele1+ele2)
    
    return cost
def main():
    # -------------------------
    # WRITE YOUR LOGIC BELOW
    # -------------------------
    arr = list(map(int, input().split()))
    print('minimum costt:', minimumCostToConnectSticks(arr))
    return 0

if __name__ == "__main__":
    # Note: These prints will go to output.txt if USE_FILE is True
    main()