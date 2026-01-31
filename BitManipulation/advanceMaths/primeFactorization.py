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

def sieve(n):

    ans = [1 for i in range(n+1)]

    ans[0] = 0
    ans[1] = 1
    for i in range(2, n+1):
        if ans[i] != 1:
            continue
        ans[i] = i
        for j in range(i*i, n+1, i):
            if ans[j] == 1:
                ans[j] = i
    print(ans)
    return ans

def factors(num, arr):

    ans = []

    while num != 1:
        ans.append(arr[num])
        num = num // arr[num]

    return ans

def main():
    # -------------------------
    # WRITE YOUR LOGIC BELOW
    # -------------------------
    arr = list(map(int, input().split()))

    sieveArr = sieve(max(arr))
    for num in arr:
        print(factors(num, sieveArr))
    return 0

if __name__ == "__main__":
    # Note: These prints will go to output.txt if USE_FILE is True
    main()