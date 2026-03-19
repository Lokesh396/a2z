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

class Node:
    def __init__(self, data=0, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev


# Don't change the code above.


def findPairs(head: Node, k: int) -> List[int]:
    """
    You are given a sorted doubly linked list of size 'n',
    consisting of distinct positive integers, and a number 'k'.
    Find out all the pairs in the doubly linked list with sum equal to 'k'.

    Algorithm:
    - Given the doubly linked list is sorted the problem boils down to 2sum
    - find the tail pointer and now we have  two pointers head and tail.
    - we will traverse from left and from the back until they dont meet.
    - we add our pairs to the ans if the value of left and right pointer equals to the k.
    - we move to next and prev accordingly.

    Args:
        head: head of the linkedlist
    
    Returns: returns the pairs with given sum

    Time Complexity: O(n)

    Space Complexity: O(n)
    """
    # Write your code here.
    # Return boolean true or false.
    temp = head
    while temp and temp.next:
        temp = temp.next
    ans = []
    while temp and head and temp != head and temp.next != head:
        avail = head.data + temp.data
        if avail == k:
            ans.append([head.data, temp.data])
            head = head.next
            temp = temp.prev
        elif avail < k:
            head = head.next
        else:
            temp = temp.prev
    return ans


def main():
    # -------------------------
    # WRITE YOUR LOGIC BELOW
    # -------------------------
    
    return 0

if __name__ == "__main__":
    # Note: These prints will go to output.txt if USE_FILE is True
    main()