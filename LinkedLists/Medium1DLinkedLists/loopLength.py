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
class Node:
    def __init__(self, data=0, next=None):
        self.val = data
        self.next = next


# Please do not change code above.

def hasCycle(head):
    fast = head
    slow = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:

            slow = head
            while slow != fast:
                slow = slow.next
                fast = fast.next
            
            return slow
    
    return None

def lengthOfLoop(head: Node) -> int:
    """
    Given the starting point of cycle return the length of the cycle.

    Algorithm:
     - we will iterate from the next pointer unitl we we reaches the starting point and we increment
     the count.
     
    Args:
        - head: head of the linkedlist
    
    Returns: returns the length of the cycle

    Time Complexity: O(n)

    Space Complexity: O(1)
    """
    # Write your code here
    slow = hasCycle(head)

    if not slow:
        return 0

    cnt = 1

    nxt = slow.next

    while nxt != slow:
        nxt = nxt.next
        cnt += 1
    
    return cnt


def main():
    # -------------------------
    # WRITE YOUR LOGIC BELOW
    # -------------------------
    
    return 0

if __name__ == "__main__":
    # Note: These prints will go to output.txt if USE_FILE is True
    main()