import sys
import os
from pathlib import Path
from collections import defaultdict
from typing import List
import heapq

# Fast I/O and Recursion Setup
sys.setrecursionlimit(2000)
input = sys.stdin.readline

USE_FILE = True

if USE_FILE:
    BASE_DIR = Path(__file__).resolve().parents[2]
    sys.stdin = open(os.path.join(BASE_DIR, "input.txt"), "r")
    sys.stdout = open(os.path.join(BASE_DIR, "output.txt"), "w")

def arrayRankTransform(arr: List[int]) -> List[int]:
    hashmap  = defaultdict(int)

    heap = []
    for num in arr:
        if num not in hashmap:
            hashmap[num]=-1
            heapq.heappush(heap, num)
    rank = 0
    while heap:
        num = heapq.heappop(heap)
        rank += 1
        hashmap[num]=rank
    
    for i in range(len(arr)):
        arr[i] = hashmap[arr[i]]
    
    return arr
        

def main():
    # -------------------------
    # WRITE YOUR LOGIC BELOW
    # -------------------------
    arr = list(map(int, input().split()))
    print('Array Transform:', arrayRankTransform(arr))
    return 0

if __name__ == "__main__":
    # Note: These prints will go to output.txt if USE_FILE is True
    main()