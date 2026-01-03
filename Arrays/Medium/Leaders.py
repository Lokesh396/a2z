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
    
def superiorElements(a):
    """
    Given an array of elements, return the array with elements which doesn't have elements greater than
    them to the right in sorted order.

    Algorithm:
    - we take 0 as curr max, we will traverse from right and check the curr max is less thatn the curr
    element or not,if it is greater that means it is greater than all the elements to the right.
    - we will update the maximum with maximum of current and maximum element.

    Args:
        a:input array

    Returns: returns the superior elements in sorted order.

    Time Complexity:O(nlgn) due to sorting, if the array is in descending order.

    Space Complexity: O(n), if stack space and merge array is considered.

    """

    next_max = 0
    output = []
    for i in range(len(a)-1, -1, -1):
        if a[i] > next_max:
            output.append(a[i])
        
        next_max = max(next_max, a[i])
    
    output.sort()
    return output
def main():
    # -------------------------
    # WRITE YOUR LOGIC BELOW
    # -------------------------
    arr = list(map(int, input().strip().split()))
    print('Leaders:', superiorElements(arr))
    return 0

if __name__ == "__main__":
    # Note: These prints will go to output.txt if USE_FILE is True
    main()