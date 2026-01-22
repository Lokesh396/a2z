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
def isPossible(arr, n, m, mid):
    """
    given arr, no of books, students, return whether it is possible to assign all books to the students.

    Algorithm:
    - we will count the no of students we can assign with the given pages.

    Args:
        arr: books with pages
        n: no of books
        m: students
        mid: no of pages we can assign to each student.
    
    Returns: return whether the all books can be assigned or not

    Time Complexity: O(n)

    Space Complexity: O(1)
    """
    csum  = arr[0]
    sc = 1
    for i in range(1,n):
        if csum + arr[i] <= mid:
            csum += arr[i]
        else:
            sc += 1
            csum = arr[i]
    return sc

def findPages(arr: list[int], n: int, m: int) -> int:
    """
    Given array of arr and no of students we need to assign the books to the students in such a way
    that the maximum no of pages assigned to student is minimum.

    Algorithm:
    - we will element the search space based on the outcome, if that is possible we need to minimize
    so we will move to the right else to the left.

    Args:
        arr: books with pages
        n: no of books
        m: students
    
    Returns: return the maximum no of pages assigned to the students so pages assigned is minimized.

    Time Complexity: O(n lgsum(n))

    Space Complexity: O(1)

    Pattern: Binary search on answers

    Subpattern: possible with max(min)
    """
    if n < m: # if no boos is less than students it is not possible
        return -1
    # Write your code here
    # Return the minimum number of pages
    low = max(arr)
    high = sum(arr)
    while low <= high:
        mid = (low + high) // 2
        sc = isPossible(arr, n, m, mid)
        if sc > m:
            low = mid + 1
        else:
            high = mid - 1
    
    return low
def main():
    # -------------------------
    # WRITE YOUR LOGIC BELOW
    # -------------------------
    arr = list(map(int, input().split()))
    s = int(input())
    print('max Pages',findPages(arr,len(arr), s))
    return 0

if __name__ == "__main__":
    # Note: These prints will go to output.txt if USE_FILE is True
    main()