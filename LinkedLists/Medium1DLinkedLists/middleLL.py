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
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Given the head of linkedlist return the middle of linked list.

        Algorithm:
        - we use hare and tortoise algo, as the slow pointer move 1 step, the fast pointer moves twice as
        much as the slow, when the fast pointer reaches the end by that time slow is at middle.

        Args:
            - head: ListNode
        
        Returns: returns the middle of the linked list.

        Time Complexity: O(n)

        Space Complexity: O(1)
        """
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        return slow

def main():
    # -------------------------
    # WRITE YOUR LOGIC BELOW
    # -------------------------
    
    return 0

if __name__ == "__main__":
    # Note: These prints will go to output.txt if USE_FILE is True
    main()