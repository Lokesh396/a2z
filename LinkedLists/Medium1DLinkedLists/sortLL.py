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

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        """
        Given the head of the linkedlist return the head of linkedlist
        after sorting.

        Algorithm:
        - we traverse until there is exactly one element or no elements.
        - we find the middle and divide them into two lists and we will repeat until step1.

        Args:
            - head: head of the linkedlist

        Returns: returns the head of linkedlist after sorting

        Time Complexity: O(nlgn)

        Space Complexity: O(1)

        """
        if not head or not head.next:
            return head
        
        # Find the middle of the linked list 
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        mid = slow.next
        slow.next = None
        
        # Sort both halves
        left = self.sortList(head)
        right = self.sortList(mid)
        
        return self.merge(left, right)
    
    def merge(self, l1: ListNode, l2: ListNode) -> ListNode:

        """
        Given heads of two sorted linkedlist, return the head of the linkedlist after
        merging.

        Algorithm:
         - we start by creating create a dummy node and traverse until both head or valid,
         we will do normal merge by comparing the elements in the both heads and update the
         accordingly.
         - finally we return the head of sorted linkedlist.

         Args:
            - l1: head of linkedlist 1
            - l2: head of linkedlist 2
        
        Time Complexity: O(n)

        Space Complexity: O(1)
        """

        dummy = ListNode(0)
        tail = dummy
        
        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next
        
        tail.next = l1 if l1 else l2
        return dummy.next

def main():
    # -------------------------
    # WRITE YOUR LOGIC BELOW
    # -------------------------
    
    return 0

if __name__ == "__main__":
    # Note: These prints will go to output.txt if USE_FILE is True
    main()