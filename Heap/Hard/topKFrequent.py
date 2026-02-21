import sys
import os
from pathlib import Path
from collections import Counter
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

def topKFrequent( nums: List[int], k: int) -> List[int]:
        frequency = Counter(nums)
        elements = [[-val, key] for key, val  in frequency.items()]
        heapq.heapify(elements)
        out = []
        while k:
            val, key = heapq.heappop(elements)
            out.append(key)
            k -= 1
        
        return out
def main():
    # -------------------------
    # WRITE YOUR LOGIC BELOW
    # -------------------------
    arr = list(map(int, input().split()))
    k = int(input())
    print('top k frequent:', topKFrequent(arr, k))
    return 0

if __name__ == "__main__":
    # Note: These prints will go to output.txt if USE_FILE is True
    main()