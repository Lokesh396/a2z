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


    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """
        Given head of two linked lists, add them together and return the new head.

        Algorithm:
         - we will traverse until one of the l1 or l2 is valid, we create new node with 
         (l1 + l2 + carry) % 10 and update the carry as (l1 + l2 + carry) // 10
         - we will update the l1 and l2 until both are invalid.
         - even after traversing if the carry still exists we create a new node and add
         them to the tail.

        Args:
            - l1: head of linkedlist 1
            - l2: head of linkedlist 2
        
        Returns: returns the head of the new linkedlist.

        Time Complexity: O(n)

        Space Complexity: O(n)

        """
        carry = 0
        head = l1
        dummy = ListNode(-1)
        head = dummy
        while l1 or l2:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            newval = val1 + val2 + carry
            dummy.next = ListNode(newval % 10)
            carry = newval // 10
            dummy = dummy.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            
        if carry:
            dummy.next = ListNode(carry)
        
        return head.next

def main():
    # -------------------------
    # WRITE YOUR LOGIC BELOW
    # -------------------------
    
    return 0

if __name__ == "__main__":
    # Note: These prints will go to output.txt if USE_FILE is True
    main()