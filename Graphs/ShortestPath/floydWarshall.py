import sys
import os
from pathlib import Path

# Fast I/O and Recursion Setup
sys.setrecursionlimit(2000)
input = sys.stdin.readline

USE_FILE = True

if USE_FILE:
    BASE_DIR = Path(__file__).resolve().parents[2]
    sys.stdin = open(os.path.join(BASE_DIR, "input.txt"), "r")
    sys.stdout = open(os.path.join(BASE_DIR, "output.txt"), "w")

def floydWarshall(dist):
    #Code here
    
    n = len(dist)
    
    for i in range(n):
        
        for j in range(n):
            for k in range(n):
                if dist[j][i] == 10**8 or dist[i][k] == 10**8: # Infinity
                    continue
                dist[j][k] = min(dist[j][k], dist[j][i] + dist[i][k])
                
def main():
    # -------------------------
    # WRITE YOUR LOGIC BELOW
    # -------------------------
    
    return 0

if __name__ == "__main__":
    # Note: These prints will go to output.txt if USE_FILE is True
    main()