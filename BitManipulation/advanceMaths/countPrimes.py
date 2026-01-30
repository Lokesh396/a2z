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

def countPrimes(n: int) -> int:
    if n < 2:
        return 0
    
    sieve  = [1 for i in range(n)]

    sieve[0] = 0
    sieve[1] = 0

    i = 2
    while i * i < n:

        if sieve[i] == 1:
            
            for j in range(i*i, n, i):
                sieve[j] = 0
        i += 1
    return sum(sieve)

def main():
    # -------------------------
    # WRITE YOUR LOGIC BELOW
    # -------------------------
    n = int(input())
    print('Number of primes:', countPrimes(n))
    return 0

if __name__ == "__main__":
    # Note: These prints will go to output.txt if USE_FILE is True
    main()