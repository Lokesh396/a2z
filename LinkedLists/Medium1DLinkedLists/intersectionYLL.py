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
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        
        headAL = 0
        headBL = 0

        temp1 = headA
        temp2 = headB

        while temp1:
            headAL += 1
            temp1 = temp1.next
        
        while temp2:
            headBL += 1
            temp2 = temp2.next
        
        diff = abs(headAL - headBL)
        if headAL > headBL:
            temp1 = headA
            temp2 = headB
        else:
            temp1 = headB
            temp2 = headA

        while diff  > 0:
            temp1 = temp1.next
            diff -= 1
        
        while temp1 and temp2:
            if temp1 == temp2:
                return temp1
            temp1 = temp1.next
            temp2 = temp2.next
        
        return None


def main():
    # -------------------------
    # WRITE YOUR LOGIC BELOW
    # -------------------------
    
    return 0

if __name__ == "__main__":
    # Note: These prints will go to output.txt if USE_FILE is True
    main()