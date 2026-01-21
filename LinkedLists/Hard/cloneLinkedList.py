import sys
import os
from pathlib import Path
from typing import Optional

# Fast I/O and Recursion Setup
sys.setrecursionlimit(2000)
input = sys.stdin.readline

USE_FILE = True

if USE_FILE:
    BASE_DIR = Path(__file__).resolve().parents[2]
    sys.stdin = open(os.path.join(BASE_DIR, "input.txt"), "r")
    sys.stdout = open(os.path.join(BASE_DIR, "output.txt"), "w")


# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        memory = dict()

        dummy = Node(-1)
        newHead = dummy
        temp = head

        while temp:
            newNode =  Node(temp.val)
            memory[temp] = newNode
            dummy.next = newNode
            temp = temp.next
            dummy = dummy.next
        
        temp = head

        while temp:
            if temp.random:
                newNode = memory[temp]
                newNode.random = memory[temp.random]
            temp = temp.next
        
        return newHead.next

def main():
    # -------------------------
    # WRITE YOUR LOGIC BELOW
    # -------------------------
    
    return 0

if __name__ == "__main__":
    # Note: These prints will go to output.txt if USE_FILE is True
    main()