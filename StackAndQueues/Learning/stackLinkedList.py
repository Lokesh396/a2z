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
    def __init__(self, data, next_node=None):
        self.data = data
        self.next = next_node

class Stack:
    # Write your code here
    def __init__(self):
    # Write your code here
        self.head = None
        self.length = 0
        
    def getSize(self):
        # Write your code here
        return self.length

    def isEmpty(self):
        # Write your code here
        return self.length == 0

    def push(self, data):
        # Write your code here
        node = Node(data)
        if self.head is None:
            self.head = node
        else:
            node.next = self.head
            self.head = node
        self.length += 1
        


    def pop(self):
        # Write your code here
        if self.head:
            self.length -= 1
            self.head = self.head.next
    def getTop(self):
        # Write your code here
        if not self.head:
            return -1
        return self.head.data
def main():
    # -------------------------
    # WRITE YOUR LOGIC BELOW
    # -------------------------
    
    return 0

if __name__ == "__main__":
    # Note: These prints will go to output.txt if USE_FILE is True
    main()