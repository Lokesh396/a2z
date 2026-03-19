import sys
import os
from pathlib import Path

# Fast I/O and Recursion Setup
sys.setrecursionlimit(2000)
input = sys.stdin.readline

USE_FILE = True

if USE_FILE:
    BASE_DIR = Path(__file__).resolve().parents[2]
    sys.stdin = open(os.path.join(BASE_DIR, "input.txt"), "r")
    sys.stdout = open(os.path.join(BASE_DIR, "output.txt"), "w")

class Node:
    def __init__(self, data=0, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev


# Don't change the code above.


def removeDuplicates(head: Node) -> Node:
    # Write your code here
    """
    You are given a sorted doubly linked list of size 'n'.
    Remove all the duplicate nodes present in the linked list.

    Algorithm:
    - we will create a dummy node and traverse until head is valid.
    - if the value of dummy and head doesn't match we will append
    the node to the dummy and head.prev as the dummy
    - if the value is same as the previous we will move forward

    Args:
        head: head of the doubly linkedlist
    
    Returns: returns the new head

    Time Complexity: O(n)
    
    Space Complexity: O(1)
    """
    dummy = Node(0)
    newhead = dummy
    while head:
        if dummy.data != head.data:
            dummy.next = head
            head.prev = dummy
            head = head.next
            dummy = dummy.next
        else:
            head = head.next
    dummy.next = None
    return newhead.next

def main():
    # -------------------------
    # WRITE YOUR LOGIC BELOW
    # -------------------------
    
    return 0

if __name__ == "__main__":
    # Note: These prints will go to output.txt if USE_FILE is True
    main()