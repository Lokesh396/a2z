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

    def middle(self, head):
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        return slow
    
    def reverse(self, head):
        prev = None
        while head:
            nxt = head.next
            head.next = prev
            prev = head
            head = nxt
        
        return prev

    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        """
        Given an linkedlist we need to check whether the linkedlist is palindrome or not.

        Algorithm:
        - we wil find element and the reverse the list from middle element.
        - we will traverse through the linkedlist and check whether both nodes has same value or not.
        - if we reach the end of one node atleast then that means that is a a palindrome.

        Args:
            - head: head of the LinkedList
        
        Returns: returns true if linkedlist is palindrome else false

        Time Complexity: O(n)

        Space Complexity: O(1)
        """
        
        middle = self.middle(head)
        reverseHead = self.reverse(middle)

        while reverseHead and head:
            if reverseHead.val != head.val:
                return False
            
            reverseHead = reverseHead.next
            head = head.next
        
        return True
def main():
    # -------------------------
    # WRITE YOUR LOGIC BELOW
    # -------------------------
    
    return 0

if __name__ == "__main__":
    # Note: These prints will go to output.txt if USE_FILE is True
    main()