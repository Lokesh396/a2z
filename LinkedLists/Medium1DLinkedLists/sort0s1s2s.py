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