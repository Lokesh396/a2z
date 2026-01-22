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

def NthRoot(n: int, m: int) -> int:
    """
    Given an number m, return the n root of the number.

    Algorithm:
    - we are sure the nth root will definitely will be in the range(1,m) that is our search space
    - at mid we will check whether the mid ** n gives us the answer and update the search
    space.

    Args:
        m: input value m
        n: no of times it can be multiplied
    
    Returns: returns the n root of the number m

    Time Complexity: O(lgx)

    Space Complexity: O(1)
    
    Pattern: Binary Search

    Subpattern: Binary Search on answers
    """
    # Write Your Code Here
    low = 1
    high = m

    while low <= high:
        
        mid = (low+high)//2

        currval = mid ** n
        if currval == m:
            return mid
        
        elif currval < m:
            low = mid + 1
        else:
            high = mid -1
    
    return -1

def main():
    # -------------------------
    # WRITE YOUR LOGIC BELOW
    # -------------------------
    n = int(input())
    m = int(input())
    """
    sample input: 
    3
    1000

    sample output:
    Nth 3 root of m 1000 is: 10
    """
    print(f'Nth {n} root of m {m} is:', NthRoot(n, m))
    return 0

if __name__ == "__main__":
    # Note: These prints will go to output.txt if USE_FILE is True
    main()