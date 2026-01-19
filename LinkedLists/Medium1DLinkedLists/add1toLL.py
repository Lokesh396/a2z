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
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next


# Don't change the code above.

def reverse(head: Node) -> Node:
    prev = None
    
    while head:
        nxt = head.next
        head.next = prev
        prev = head
        head = nxt

    return prev

def addOne(head: Node) -> Node:
    # write your code here
    
    head = reverse(head)
    carry = 1

    temp = head
    prev = None
    while temp and carry:
        new_val = temp.data + carry
        if new_val <= 9:
            temp.data = new_val
            carry = 0
            break
        else:
            ld = new_val % 10 
            temp.data = ld
            carry = new_val // 10
        prev = temp
        temp = temp.next
    node = Node(0)
    if carry:
        node.data = carry
        prev.next = node
        return reverse(head)
    else:
        return reverse(head)
def main():
    # -------------------------
    # WRITE YOUR LOGIC BELOW
    # -------------------------
    
    return 0

if __name__ == "__main__":
    # Note: These prints will go to output.txt if USE_FILE is True
    main()