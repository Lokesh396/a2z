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
    def __init__(self, data):
        self.data = data
        self.next = None
        

def sortList(head):
    """
    Given the head of linkedlist containing only 0'1, 1's and 2`s group zeroes, ones and twos together
    and return the sorted list.

    Algorithm:
    - we will take three pointers one for each [0, 1, 2] head and tail and traverse through the 
    linkedlist and update the pointers accordingly.
    - twos tail will be pointing to None
    - ones tail will be pointing to twos head
    - zeores tail will be pointing to ones head

    - we will finally return the head of the zeros.

    Args:
        - head: head of the linkedlist

    Returns: returns the head of the linkedlist after sorting

    Time Complexity: O(n)

    Space Complexity: O(1)
    """
    # Write your code here
    zeroes = Node(0)
    zeroTail = zeroes
    ones = Node(1)
    oneTail = ones
    twos= Node(2)
    twotail = twos

    while head:
        if head.data == 0:
            zeroTail.next = head
            zeroTail = zeroTail.next
        elif head.data == 1:
            oneTail.next = head
            oneTail = oneTail.next
        else:
            twotail.next = head
            twotail = twotail.next
        
        head =  head.next
    twotail.next = None
    oneTail.next = twos.next
    zeroTail.next = ones.next
    
    return zeroes.next

def main():
    # -------------------------
    # WRITE YOUR LOGIC BELOW
    # -------------------------
    
    return 0

if __name__ == "__main__":
    # Note: These prints will go to output.txt if USE_FILE is True
    main()