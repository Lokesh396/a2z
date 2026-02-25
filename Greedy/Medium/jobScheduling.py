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

def jobScheduling(jobs):

    # Write your code here
    # Return an integer denoting the maximum pofit  
    jobs = sorted(jobs, key = lambda job : -job[2])

    mx = 0
    for job in jobs:
        mx = max(job[1], mx)
    
    slots = [-1 for i in range(mx)]
    cnt, profit = 0, 0
    for job in jobs:
        idx = job[1]-1
        if slots[idx] ==-1:
            slots[idx] = job[1]
            cnt += 1
            profit += job[2]
        else:
            for j in range(idx, -1, -1):
                if slots[j] == -1:
                    slots[j] = job[1]
                    cnt += 1
                    profit += job[2]
                    break

    return [cnt, profit]

def main():
    # -------------------------
    # WRITE YOUR LOGIC BELOW
    # -------------------------
    id = list(map(int, input().split()))
    dl = list(map(int, input().split()))
    pt = list(map(int, input().split()))
    print('Jobs and Profit:', jobScheduling(list(zip(id,dl,pt))))
    return 0

if __name__ == "__main__":
    # Note: These prints will go to output.txt if USE_FILE is True
    main()