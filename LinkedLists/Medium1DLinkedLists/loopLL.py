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
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        """
        Given the head of the linked list we need to return whether there is a cycle.

        Algorithm:
         - we use the hare and tortoise algorithm, and check whether they meet at any point,
         if they meet at a point then there is a cycle.
         - if the fast pointer reaches the end it means there is no cycle.
        
        Args:
            - head: head node of the linked list.
        
        Returns: returns if a cycle exists or not

        Time Complexity: O(n)

        Space Complexity: O(1)
        """
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        
        return False

def main():
    # -------------------------
    # WRITE YOUR LOGIC BELOW
    # -------------------------
    
    return 0

if __name__ == "__main__":
    # Note: These prints will go to output.txt if USE_FILE is True
    main()