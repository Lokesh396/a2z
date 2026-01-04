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
def generate_row(n):
    """
    Given a number, generate that row in pascals triangle.

    Algorithm:
    - first element will be one in every row, the next element is simply row - i / i where i is the
    col number.

    Args:
        n : row number
    
    Returns: an array with elements in that row of pascals triangle

    Time Complexity: O(n)

    Space Complexity: O(n)

    """
    ans = [1]
    prev = 1
    for i in range(1,n):
        prev = prev * (n-i)
        prev = prev // i
        ans.append(prev)
    return ans

        

def generate( numRows):
    """
    Given no. of numbers generate the pascals triangle.

    Algorithm:
    - we will generate every row and append that too result.

    Args:
        numRows: no of rows that needs to be generated.

    Returns: returns the complete pascals triangle.

    Time Complexity: O(n^2)
    
    Space Complexity: O(n^2)
    """
    ans = []
    for i in range(numRows):
        row = generate_row(i+1)
        ans.append(row)
    return ans

def getElementatRowCol(row, col):
    """
    Given row and column not 0 based, return the number at that row and col.

    Algorithm:
    - It works based on the principle of ncr = n! / r! * (n-r!)

    Args:
        row: row number
        col: col number

    Retruns: returns element at that row and col

    Time Complexity: O(col)
    
    Space Complexity: O(1)
    """
    ans = 1
    for i in range(1,col):
        ans = ans * (row-i)
        ans = ans // i
    return ans
def main():
    # -------------------------
    # WRITE YOUR LOGIC BELOW
    # -------------------------
    n = int(input())
    print('Pascals Triangle:', generate(n))
    print('Row and col Value at 6,4:', getElementatRowCol(6,4))
    return 0

if __name__ == "__main__":
    # Note: These prints will go to output.txt if USE_FILE is True
    main()