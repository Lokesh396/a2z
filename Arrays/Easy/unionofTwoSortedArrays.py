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

def appendValue(output, val):
    """
    
    Helper function to store the unique elements.

    Args:
        output: Array that stores the unique elements.
        val: value that needed to be added in to the output.
    """

    if len(output) == 0 or  output[-1] != val:
        output.append(val)

def sortedArray(a, b):
    """
    
    Given two sorted arrays and return the union of these arrays.

    Algorithm:
    - Given the arrays the arrays already sorted, we can use the `merge` technique to
    store the union of elements.
    - Before adding each number to the output arrays we need to make sure it is not
    already `presnet` in the array.

    Args:
        a: array 1
        b: array 2
    
    Returns:
        out: Returns the union of araray `a` and `b`.

    Time Complexity: O(m+n) given length of array a is `m` and b is `n`.

    Space Complexity: O(m+n) if both the array elements are unique this is
    the maximum space required.

    """

    m = len(a)
    n = len(b)

    i, j = 0, 0

    output = []

    while i < m and j < n:
        val = 0
        if a[i] < b[j]:
            val = a[i]
            i += 1
        else:
            val = b[j]
            j += 1
        appendValue(output, val)        

    
    while i < m:
       appendValue(output, a[i])
       i += 1

    
    while j < n:
        appendValue(output, b[j])
        j += 1

    
    return output
def main():
    # -------------------------
    # WRITE YOUR LOGIC BELOW
    # -------------------------
    arr1 = list(map(int, input().split()))
    arr2 = list(map(int, input().split()))
    print("Union", sortedArray(arr1, arr2))
    return 0

if __name__ == "__main__":
    # Note: These prints will go to output.txt if USE_FILE is True
    main()