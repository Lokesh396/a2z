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

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return
        stack = []
        inorder= None
        stack.append(root)
        while stack:
            node = stack.pop()
            if not inorder:
                inorder = node
            else:
                inorder.left = None
                inorder.right = node
                inorder = inorder.right
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
    

    def flattenv1(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        curr = root

        while curr:

            if curr.left:
                prev = curr.left
                while prev.right:
                    prev = prev.right
                
                prev.right = curr.right
                curr.right = curr.left
                curr.left = None
            
            curr = curr.right

def main():
    # -------------------------
    # WRITE YOUR LOGIC BELOW
    # -------------------------
    
    return 0

if __name__ == "__main__":
    # Note: These prints will go to output.txt if USE_FILE is True
    main()