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
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Given the head of the linkedlist delete the middle node

        Algorithm:
        - we use hare and tortoise algorithm and store the prev node, at the time fast reaches the end,
        the slow is at the middle and the prev is at one step before the slow.
        - if slow is same as head that means there is only one node.
        - we will change the refrence of next node in the prev node.

        Args:
            - head:  head of the linkedlist
        
        Returns: returns the head of the linkedlist

        Time Complexity: O(n)

        Space Complexity: O(1)
        """
        slow = fast = head
        prev = None

        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        if slow == fast:
            return slow.next
        prev.next = prev.next.next

        return head

def main():
    # -------------------------
    # WRITE YOUR LOGIC BELOW
    # -------------------------
    
    return 0

if __name__ == "__main__":
    # Note: These prints will go to output.txt if USE_FILE is True
    main()