import sys
import os
from pathlib import Path
from typing import Optional, List

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
    def preorderTraversalIter(self, root: Optional[TreeNode]) -> List[int]:
        
        if not root:
            return []
        
        q = []
        q.append(root)
        out = []

        while q:
            curr = q.pop()
            out.append(curr.val)
            if curr.right:
                q.append(curr.right)
            if curr.left:
                q.append(curr.left)
        
        return out
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        

        def preorder(root, out):
            if not root:
                return out
            out.append(root.val)
            if root.left:
                preorder(root.left, out)
            if root.right:
                preorder(root.right, out)
            
            return out
        
        return preorder(root, [])
    
def main():
    # -------------------------
    # WRITE YOUR LOGIC BELOW
    # -------------------------
    
    return 0

if __name__ == "__main__":
    # Note: These prints will go to output.txt if USE_FILE is True
    main()