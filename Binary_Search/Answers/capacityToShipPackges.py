import sys
import os
from pathlib import Path
from typing import List

# Fast I/O and Recursion Setup
sys.setrecursionlimit(2000)
input = sys.stdin.readline

USE_FILE = True

if USE_FILE:
    BASE_DIR = Path(__file__).resolve().parents[2]
    sys.stdin = open(os.path.join(BASE_DIR, "input.txt"), "r")
    sys.stdout = open(os.path.join(BASE_DIR, "output.txt"), "w")

def ispossible(weights, cap, days):
    """
    Given weights and the cap, need to return if it possible to ship the packages in given days.

    Algorithm:
    - given the cap we will calculate how many days does it take for all the cargo to be shipped
    
    Args:
        weights: weights of the cargo
        cap: ship capacity
        days: no of days
    
    Returns: returns true if it is possible to ship that many packages in the given days.

    Time Complexity: O(n) # n is the size of the weights

    Space Complexity: O(1)

    """

    dc = 0
    lc = 0
    for weight in weights:
        lc += weight
        if lc >  cap:
            dc += 1
            lc = weight
    return dc+1 <= days

        

def shipWithinDays(weights: List[int], days: int) -> int:
    """
    Given the weights and no of days , we need to return the minimum capacity of the ship

    Algorithm:
    - The search space is max of weights and sum of  the weights.
    - we will calculate mid and check if it is possible to ship all the packages, in order to find
    the minimum we will decrease search space accordingly.
    - at first low is at not possible high is at possible, due to opoosite polarity low will be at
    the first posisble answer.

    Args:
        weights: weights of the cargo
        days: no of days
    
    Returns: returns the minimum capacity of the ship

    Time Complexity: O(lg sum(weights) * n)

    Space Complexity: O(1)

    Pattern: Binary Search

    Subpattern: Binary Search on answers (possible or not possible)
    """
    low  = max(weights)
    high = sum(weights)

    while low <= high:

        mid = (low + high)//2

        if ispossible(weights,mid, days):
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
    print('least no. of days required is: ', shipWithinDays(arr, h))
    return 0

if __name__ == "__main__":
    # Note: These prints will go to output.txt if USE_FILE is True
    main()