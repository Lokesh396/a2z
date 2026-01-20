import sys
import os
from pathlib import Path
from typing import List

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


def findPairs(head: Node, k: int) -> List[int]:

    # Write your code here.
    # Return boolean true or false.
    temp = head
    while temp and temp.next:
        temp = temp.next
    ans = []
    while temp and head and temp != head and temp.next != head:
        avail = head.data + temp.data
        if avail == k:
            ans.append([head.data, temp.data])
            head = head.next
            temp = temp.prev
        elif avail < k:
            head = head.next
        else:
            temp = temp.prev
    return ans


def main():
    # -------------------------
    # WRITE YOUR LOGIC BELOW
    # -------------------------
    
    return 0

if __name__ == "__main__":
    # Note: These prints will go to output.txt if USE_FILE is True
    main()