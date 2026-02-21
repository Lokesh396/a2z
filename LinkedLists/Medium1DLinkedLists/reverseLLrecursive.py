import sys
import os
from pathlib import Path
from typing import Optional

# Fast I/O and Recursion Setup
sys.setrecursionlimit(2000)
input = sys.stdin.readline

USE_FILE = True

if USE_FILE:
    BASE_DIR = Path(__file__).resolve().parents[2]
    sys.stdin = open(os.path.join(BASE_DIR, "input.txt"), "r")
    sys.stdout = open(os.path.join(BASE_DIR, "output.txt"), "w")
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverse(self, curr, prev):
        """
        Given the node we need to swap the pointers to the next with the prev.

        Algorithm:
        - we will recursively traverse until the curr becomes none which means we reached the end of the
        node.
        - we will swap the next with the prev and make the next as our current.

        Args:
            curr: curr head
            prev: prev pointer
        
        Returns: returns the head of the reversed list.

        Time Complexity: O(n)

        Space Complexity O(n)
        """
        if not curr:
            return prev
        nxt = curr.next
        curr.next = prev
        return self.reverse(nxt, curr)
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        return self.reverse(head,None)
def main():
    # -------------------------
    # WRITE YOUR LOGIC BELOW
    # -------------------------
    
    return 0

if __name__ == "__main__":
    # Note: These prints will go to output.txt if USE_FILE is True
    main()