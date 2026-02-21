import sys
import os
from pathlib import Path
from typing import *

# Fast I/O and Recursion Setup
sys.setrecursionlimit(2000)
input = sys.stdin.readline

USE_FILE = True

if USE_FILE:
    BASE_DIR = Path(__file__).resolve().parents[2]
    sys.stdin = open(os.path.join(BASE_DIR, "input.txt"), "r")
    sys.stdout = open(os.path.join(BASE_DIR, "output.txt"), "w")

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Given the head of the Linkedlist we need to reverse the linkedlist and return the new head, we must
        not create new nodes with the same values, references should be same.

        Algorithm:
        - we take prev as none and start with the current node, we will the save the next node and curr node
        next will be the prev, as now current node becomes the prev and next node become the curr.
        - finally we return the prev node which stores the new head.

        Args:
            - head: head of LinkedList

        Time Complexity: O(n)

        Space Complexity: O(1)
        """
        prev = None
        curr = head

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        return prev

# Definition for singly-linked list.


def main():
    # -------------------------
    # WRITE YOUR LOGIC BELOW
    # -------------------------
    
    return 0

if __name__ == "__main__":
    # Note: These prints will go to output.txt if USE_FILE is True
    main()