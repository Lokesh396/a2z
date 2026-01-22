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
def isPossible(bloomDay, m, k, mid):
    """
    Given bloomDay, m, k and the day, need to return no of boques can be made.

    Algorithm:
    - given the day we will calculate how many boquets can we make, in order to make a boque we
    need to have k adjacent flowers.
    
    Args:
        bloomDay: array of flower bloomDays
        mid: the current day
        k: adjacent flower length
        m: the total boquets required
    
    Returns: returns True if it is possible to make the required boquets.

    Time Complexity: O(n) # n is the size of the bloomDay

    Space Complexity: O(1)
    """
    count = 0
    bc = 0 
    for num in bloomDay:
        if mid >= num:
            count += 1
        else:
            count = 0
        
        if count == k:
            bc += 1
            count = 0

    return bc >= m

    


def minDays( bloomDay: List[int], m: int, k: int) -> int:
    """
    Given flowers with their bloomDay, m is no of boquets required and k the adjacent flowers required
    to make a boquet return the no of days required to make all boquets.

    Algorithm:
    - The search space is from min to max of bloomDay, in order to make a boquets atleast we need a
    single flower even if k is 1, the min day is the day where atleast one flower is boomed.
    - we do a binary search on the search space and check for the minimum no of days required
    to complete all boquets

    Args:
        bloomDay: array with bloomday of flowers
        m: no of boquets required
        k: adjacent flowers required to make boquet
    
    Returns: minimum no of days required to make m boquets.

    Time Compexity: O(lg max(bloomDay) * n)

    Space Complexity: O(1)

    Pattern: Binary Search

    Subpattern: Binary Search on answers (possible or not possible)
    """
    if m * k > len(bloomDay):
        return -1 
    
    high = max(bloomDay)
    low = min(bloomDay)
    ans = -1
    while low <= high:

        mid = (low + high) // 2
        possible = isPossible(bloomDay, m, k , mid)

        if possible:
            ans = mid
            high = mid - 1
        else:
            low = mid + 1
    
    return ans
def main():
    # -------------------------
    # WRITE YOUR LOGIC BELOW
    # -------------------------
    arr = list(map(int, input().split()))
    m = int(input()) # boquet count
    k = int(input()) # adjacent days

    print('Minimum Days required is: ', minDays(arr, m, k))
    return 0
    return 0

if __name__ == "__main__":
    # Note: These prints will go to output.txt if USE_FILE is True
    main()