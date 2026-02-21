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
        
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return [True, slow]
        
        return [False, None]

    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Given the head of linkedlist return the starting point of the linked list if there is a cycle.

        Algorithm:
         - if we detect the cycle we will intialize a pointer at the head and traverse both pointers at
         the same speed until they are not same.
         - we will return the node they meet.

        Args:
            head: head of the linkedlist.
    
        Returns: returns the starting point of the linkedlist if exists else None
    
        Time Complexity: O(n)

        Space Complexity: O(1)
        """
        hasCycle, slow = self.hasCycle(head)
        if not hasCycle:
            return None
        
        slow1 = head
        while slow1 != slow:
            slow1 = slow1.next
            slow = slow.next
        
        return slow1
        
        
def main():
    # -------------------------
    # WRITE YOUR LOGIC BELOW
    # -------------------------
    
    return 0

if __name__ == "__main__":
    # Note: These prints will go to output.txt if USE_FILE is True
    main()