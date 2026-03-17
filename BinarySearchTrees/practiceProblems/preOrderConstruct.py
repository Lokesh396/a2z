import sys
import os
from pathlib import Path
from typing import List, Optional

# Fast I/O and Recursion Setup
sys.setrecursionlimit(2000)
input = sys.stdin.readline

USE_FILE = True

if USE_FILE:
    BASE_DIR = Path(__file__).resolve().parents[2]
    sys.stdin = open(os.path.join(BASE_DIR, "input.txt"), "r")
    sys.stdout = open(os.path.join(BASE_DIR, "output.txt"), "w")

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def insertNode(self,node):
        Node = TreeNode(node)
        if not self.root:
            self.root = Node
            return
        temp = self.root
        while temp:
            if temp and temp.val > node:
                if temp.left is None:
                    temp.left = Node
                    return
                temp = temp.left
            elif temp and temp.val < node:
                if temp.right is None:
                    temp.right = Node
                    return
                temp = temp.right
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        self.root = None

        for node in preorder:
            self.insertNode(node)
        
        return self.root

def main():
    # -------------------------
    # WRITE YOUR LOGIC BELOW
    # -------------------------
    
    return 0

if __name__ == "__main__":
    # Note: These prints will go to output.txt if USE_FILE is True
    main()