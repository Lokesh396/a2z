import sys
import os
from pathlib import Path
from collections import defaultdict

# Fast I/O and Recursion Setup
sys.setrecursionlimit(2000)
input = sys.stdin.readline

USE_FILE = True

if USE_FILE:
    BASE_DIR = Path(__file__).resolve().parents[2]
    sys.stdin = open(os.path.join(BASE_DIR, "input.txt"), "r")
    sys.stdout = open(os.path.join(BASE_DIR, "output.txt"), "w")

def beautySum(s: str) -> int:
    """
    Given a string we need to return the sum of the differences of max and min frequencies of all substrings.

    Algorithm:
    - we will iterathe through and go through each substring and calculate the difference of the max
    and min frequencies and sum it up to the total.

    Args:
        - s: input string
    
    Returns: return the total

    Time Complexity: O(n^2)

    Space Complexity: O(n)
    """
    n = len(s)
    total = 0
    for i in range(n):
        frequency = defaultdict(int)

        for j in range(i, n):
            frequency[s[j]] += 1
            maxf = max(frequency.values())
            minf = min(frequency.values())
            total += (maxf - minf)
    
    return total

def main():
    # -------------------------
    # WRITE YOUR LOGIC BELOW
    # -------------------------
    s = input()
    print('Beauty Sum:', beautySum(s))
    return 0

if __name__ == "__main__":
    # Note: These prints will go to output.txt if USE_FILE is True
    main()