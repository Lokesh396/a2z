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
    def leftheight(self, node):
        self.left = 0
        while node:
            self.left += 1
            node = node.left
        
        return self.left
    def rightheight(self, node):
        self.right = 0
        while node:
            self.right += 1
            node = node.right
        return self.right
    def countNodes(self, root: Optional[TreeNode]) -> int:
        
        if not root:
            return 0
        
        lh = self.leftheight(root)
        rh = self.rightheight(root)

        if lh == rh:
            return  (1<<lh) -1
        
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)

def main():
    # -------------------------
    # WRITE YOUR LOGIC BELOW
    # -------------------------
    
    return 0

if __name__ == "__main__":
    # Note: These prints will go to output.txt if USE_FILE is True
    main()