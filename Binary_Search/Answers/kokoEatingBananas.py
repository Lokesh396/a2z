import sys
import os
from pathlib import Path
from math import ceil
from typing import List

# Fast I/O and Recursion Setup
sys.setrecursionlimit(2000)
input = sys.stdin.readline

USE_FILE = True

if USE_FILE:
    BASE_DIR = Path(__file__).resolve().parents[2]
    sys.stdin = open(os.path.join(BASE_DIR, "input.txt"), "r")
    sys.stdout = open(os.path.join(BASE_DIR, "output.txt"), "w")

def min_time( piles, mid):
    """
    Given piles and the speed, need to return the time taken for completing
    all bananas.

    Algorithm:
    - given the speed we will calculate how many hours does it take for each pile and
    sum it up.
    
    Args:
        piles: piles of bananas
        mid: eating speed
    
    Returns: returns the minimum taken to complete eating all bananas.

    Time Complexity: O(n) # n is the size of the piles

    Space Complexity: O(1)

    """

    totalTime = 0
    for pile in piles:
        totalTime += ceil(pile/mid)
    return totalTime

def minEatingSpeed( piles: List[int], h: int) -> int:
    """
    Given the piles and no of hours guards wont be there, we need to return the eating speed
    for one hour.

    Algorithm:
    - The search space is minimum koko can eat 1 banana and maximum the max(piles).
    - we will calculate mid and check if it is possible to eat all the bananas, in order to find
    the minimum we will decrease search space accordingly.
    - at first low is at not possible high is at possible, due to opoosite polarity low will be at
    the first posisble answer.

    Args:
        piles: piles of bananas
        h: hours
    
    Returns: returns the eating speed for koko

    Time Complexity: O(lg max(piles) * n)

    Space Complexity: O(1)

    Pattern: Binary Search

    Subpattern: Binary Search on answers (possible or not possible)
    """
    high = max(piles)
    low = 1

    while low <= high:

        mid = (low + high) // 2
        totalTime = min_time(piles, mid)
        if totalTime <= h:
            high = mid - 1
        else:
            low = mid + 1
    
    return low


def main():
    # -------------------------
    # WRITE YOUR LOGIC BELOW
    # -------------------------
    arr = list(map(int, input().split()))
    h = int(input())
    print('Minimum eating speed required is: ', minEatingSpeed(arr, h))
    return 0

if __name__ == "__main__":
    # Note: These prints will go to output.txt if USE_FILE is True
    main()