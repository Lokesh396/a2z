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
    def __init__(self, val=0, next=None, child=None):
        self.data = val
        self.next = next
        self.child = child


# Don't change the code above.

def mergeTwoLists(head1, head2):
    dummy = Node(-1)
    head = dummy

    while head1 and head2:
        if head1.data > head2.data:
            dummy.child = head2
            dummy.next = None
            head2 = head2.child
        else:
            dummy.child = head1
            dummy.next = None
            head1 = head1.child
        

        dummy = dummy.child
    
    if head1:
        dummy.child = head1
    if head2:
        dummy.child = head2
    
    return head.child


def flattenLinkedList(head: Node) -> Node:
    # Write your code here
    while head and head.next:
        nxt = head.next.next
        newHead = mergeTwoLists(head, head.next)
        newHead.next = nxt
        head = newHead
    
    return head
    


def main():
    # -------------------------
    # WRITE YOUR LOGIC BELOW
    # -------------------------
    
    return 0

if __name__ == "__main__":
    # Note: These prints will go to output.txt if USE_FILE is True
    main()