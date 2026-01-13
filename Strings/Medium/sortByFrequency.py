import sys
import os
from pathlib import Path
from collections import Counter
import heapq

# Fast I/O and Recursion Setup
sys.setrecursionlimit(2000)
input = sys.stdin.readline

USE_FILE = True

if USE_FILE:
    BASE_DIR = Path(__file__).resolve().parents[2]
    sys.stdin = open(os.path.join(BASE_DIR, "input.txt"), "r")
    sys.stdout = open(os.path.join(BASE_DIR, "output.txt"), "w")

def frequencySort(s: str) -> str:
    heap = []
    frequency = Counter(s)
    for k, v in frequency.items():
        heapq.heappush(heap, (-v, k))
    
    out = ''
    while len(heap):
        v, k = heapq.heappop(heap)
        out += (k * -v)
    
    return out

def main():
    # -------------------------
    # WRITE YOUR LOGIC BELOW
    # -------------------------
    s = input()
    print('Frequency sort:', frequencySort(s))
    return 0

if __name__ == "__main__":
    # Note: These prints will go to output.txt if USE_FILE is True
    main()