import sys
import os
from pathlib import Path
from heapq import heappush, heappop

# Fast I/O and Recursion Setup
sys.setrecursionlimit(2000)
input = sys.stdin.readline

USE_FILE = True

if USE_FILE:
    BASE_DIR = Path(__file__).resolve().parents[2]
    sys.stdin = open(os.path.join(BASE_DIR, "input.txt"), "r")
    sys.stdout = open(os.path.join(BASE_DIR, "output.txt"), "w")
def isPossible(arr, mid):
    cnt = 0
    for i in range(1, len(arr)):
        diff = int((arr[i] - arr[i-1]) / mid)
        if diff * mid == (arr[i]-arr[i-1]) :
            diff -= 1
        cnt += diff
    
    return cnt

def minimiseMaxDistance(arr: list[int], k: int) -> float:
    
    # howMany = [0 for i in range(len(arr)-1)]
    # heap = []
    # for i in range(len(arr)-1):
    #     diff = arr[i+1] - arr[i]
    #     heappush(heap, (-diff, i))
    # for i in range(k):
    #     oldDis, oldInd = heappop(heap)
    #     howMany[oldInd] += 1
    #     newDiff = float(arr[oldInd+1]-arr[oldInd]) / (howMany[oldInd] + 1)
    #     heappush(heap, (-newDiff, oldInd))

    # return -heappop(heap)[0]
    diff = 1e-6
    n = len(arr)
    low = 0
    high = 0

    for i in range(n-1):
        d = arr[i+1] - arr[i]
        high = max(high, d)
    
    while high - low > diff:
        mid = (low + high) / 2.0
        
        pos = isPossible(arr, mid)
        if pos > k:
            low = mid
        else:
            high = mid
    
    return high




def main():
    # -------------------------
    # WRITE YOUR LOGIC BELOW
    # -------------------------
    arr = list(map(int, input().split()))
    s = int(input())
    print('max Distance',minimiseMaxDistance(arr, s))
    return 0

if __name__ == "__main__":
    # Note: These prints will go to output.txt if USE_FILE is True
    main()