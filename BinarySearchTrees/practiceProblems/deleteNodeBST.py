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

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:

    def constructTree(self,root):
        left = None
        if root.left:
            
            curr = root.left
            while curr.right:
                curr = curr.right
            
            curr.right = root.right
            return root.left
        elif root.right:
            curr = root.right
            while curr.left:
                curr = curr.left
            
            curr.left = root.left
            return root.right
        else:
            return None
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        
        if not root:
            return root
        
        if root.val == key:
            return self.constructTree(root)
        
        curr = root

        while curr:
            if curr.left and curr.left.val == key:
                curr.left = self.constructTree(curr.left)
                return root
            elif curr.right and curr.right.val == key:
                curr.right = self.constructTree(curr.right)
                return root
            
            if curr.val > key:
                curr = curr.left
            else:
                curr = curr.right
        
        return root
        

def main():
    # -------------------------
    # WRITE YOUR LOGIC BELOW
    # -------------------------
    
    return 0

if __name__ == "__main__":
    # Note: These prints will go to output.txt if USE_FILE is True
    main()