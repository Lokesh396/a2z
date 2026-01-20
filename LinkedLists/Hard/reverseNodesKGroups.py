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

    def reverse(self, curr):
        prev = None
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        
        return prev
    
    def returnKNode(self, head, k):
        k -= 1

        while head and k != 0:
            head = head.next
            k -= 1
        
        if k == 0: return head
        else: None

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        dummy = ListNode(-1)
        newhead = dummy
        while head:
            kNode = self.returnKNode(head, k)
            if kNode:
                nxtHead = kNode.next
                kNode.next = None

                reversehead = self.reverse(head)

                dummy.next = reversehead
                dummy = head
                head = nxtHead
            else:
                dummy.next = head
                head = None
        
        return newhead.next
        

def main():
    # -------------------------
    # WRITE YOUR LOGIC BELOW
    # -------------------------
    
    return 0

if __name__ == "__main__":
    # Note: These prints will go to output.txt if USE_FILE is True
    main()