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
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """
        Given the head of the linked list remove n node from end.

        Algorithm:
         - we traverse n steps ahead, and take another pointer which starts from head, at the time
         when the ahead pointer has no next and it becomes none, our second pointer will be standing at exactly before nth node.
         - we just change the next pointer and our task is done.

         Args:
            head: head of linkedlist
            n: node to be delete
        
        Returns: returns the head afte the n node.

        Time Complexity: O(n)

        Space Complexity: O(1)
        """
        ahead = wait = head

        for i in range(n):
            ahead = ahead.next

        if not ahead:
            return head.next
        
        while ahead and ahead.next:
            ahead = ahead.next
            wait = wait.next
        
        wait.next = wait.next.next
        return head

def main():
    # -------------------------
    # WRITE YOUR LOGIC BELOW
    # -------------------------
    
    return 0

if __name__ == "__main__":
    # Note: These prints will go to output.txt if USE_FILE is True
    main()