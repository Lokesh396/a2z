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


def deleteAllOccurrences(head: Node, k: int) -> Node:
    """
    You're given a doubly-linked list and a key 'k'.
    Delete all the nodes having data equal to 'k'.

    Algorithm:
     - we create a dummy node and add head to the dummy next.
     - we will iterate through the linkedlist and check if the next nodes value
     is same as the given k, if the value is same as the given k we will move
     the current nodes next pointer to its next's next, the next's next prev
     to the curr node.
     - if the node.next value is not same we will move forward.

     Args:
        head: head of the linkedlist
        k : value of the node that needs to be deleted.
    
    Returns: returns the new head after deleting the nodes.

    Time Complexity: O(n)

    Space Complexity: O(1)

    """
    # Write your code here
    dummy = Node(0)
    head1 = dummy
    dummy.next = head

    while dummy and dummy.next:
        if dummy.next.data == k:
            dummy.next = dummy.next.next
            if dummy.next:
                dummy.next.prev = dummy
        else:
            dummy = dummy.next
    
    return head1.next
            


def main():
    # -------------------------
    # WRITE YOUR LOGIC BELOW
    # -------------------------
    
    return 0

if __name__ == "__main__":
    # Note: These prints will go to output.txt if USE_FILE is True
    main()