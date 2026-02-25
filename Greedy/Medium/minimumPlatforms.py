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

def calculateMinPatforms(at, dt, n):
    # Write your code here.
    sweep = [0 for i in range(2401)]

    for start, end in zip(at, dt):
        sweep[start] += 1
        sweep[end+1] -= 1
    mx = sweep[0] 
    for i in range(1, 2401):
        sweep[i] += sweep[i-1]
        mx = max(mx, sweep[i])
    
    return mx

def calculateMinPatformsv2(at, dt, n):
    # Write your code here.
    at.sort()
    dt.sort()
    platoforms, mxplatforms = 1, 1
    i = 1
    j = 0
    while i < n and j < n:
        if at[i] <= dt[j]:
            platoforms += 1
            i += 1
        else:
            platoforms -= 1
            j += 1
        mxplatforms = max(mxplatforms, platoforms)
    return mxplatforms
def main():
    # -------------------------
    # WRITE YOUR LOGIC BELOW
    # -------------------------
    at = list(map(int, input().split()))
    dt = list(map(int, input().split()))
    print('Minimum Platforms:', calculateMinPatforms(at,dt, len(at)))
    return 0

if __name__ == "__main__":
    # Note: These prints will go to output.txt if USE_FILE is True
    main()