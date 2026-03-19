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

def insert(stack, val):
    """
    we will pop elements in the stack when an new element is arrived and append that value
    in the stack first, and we push back elements into the stack from last popped to first.

    Args:
        Stack: stack holding elements
        val: new val to push into stack.

    Returns: None

    Time Complexity : O(n^2)

    Space Complexity : O(n)
    """
    if not stack:
        stack.append(val)
        return
    temp = stack.pop()
    insert(stack,val)
    stack.append(temp)

def reverseStack(stack: List[int]) -> None:
    # Write your code here.
    """
    Given a stack reverse the values in the stack.

    Algorithm:
     - we will recursively pop elements from the stack until there is no elements and pass the same stack to the insert
     function which will order the elements in the stack.
      
    Args:
        stack: input stack
    
    Retuns: None

    Time Complexity: O(n)

    Space Complexity:O(n)
    """
    if stack:
        val = stack.pop()
        reverseStack(stack)
        insert(stack, val)
def main():
    # -------------------------
    # WRITE YOUR LOGIC BELOW
    # -------------------------
    
    return 0

if __name__ == "__main__":
    # Note: These prints will go to output.txt if USE_FILE is True
    main()