import sys
import os
from pathlib import Path

# Fast I/O and Recursion Setup
sys.setrecursionlimit(2000)
input = sys.stdin.readline

USE_FILE = True

if USE_FILE:
    BASE_DIR = Path(__file__).resolve().parents[1]
    sys.stdin = open(os.path.join(BASE_DIR, "input.txt"), "r")
    sys.stdout = open(os.path.join(BASE_DIR, "output.txt"), "w")

def main():
    # -------------------------
    # WRITE YOUR LOGIC BELOW
    # -------------------------

    arr = map(int, input().split())
    memory = dict()
    for num in arr:
        memory[num] = memory.get(num, 0) + 1

    maxFreq = 0
    fmax = 0
    fmin = 0
    minFreq = float('inf')
    for k, v in memory.items():
        print(k,v,fmin,fmax, 'before')
        if v > maxFreq:
            fmax = k
            maxFreq = v
    
        if v < minFreq:
            fmin = k
            minFreq = v
        print(k,v,fmin,fmax, 'after')
        
    print([fmin, fmax])
    return 0

if __name__ == "__main__":
    # Note: These prints will go to output.txt if USE_FILE is True
    main()