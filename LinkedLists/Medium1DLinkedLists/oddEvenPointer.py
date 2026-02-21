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
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Given head of the linkedlist we need return new head after reordering by maintaing relative
        order of elements in the linkedlist, first element is considered as odd element.

        Algorithm:
         - we take odd as head and even as head.next, we will continue until even and even.next is available
         - odd.next is eve.next and we updated the odd, even.next is odd.next
         - finally we will link odd.next with evenhead

        Args:
            - head: head of linked list
        
        Time Complexity: O(n)

        Space Complexity: O(1)
        """
        if not head:
            return head
        odd = head
        even = head.next
        evenhead = even
        while even and even.next:
            odd.next = even.next
            odd = odd.next
            
            even.next = odd.next
            even = even.next
        odd.next = evenhead

        return head

def main():
    # -------------------------
    # WRITE YOUR LOGIC BELOW
    # -------------------------
    
    return 0

if __name__ == "__main__":
    # Note: These prints will go to output.txt if USE_FILE is True
    main()