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
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        

        self.fst = None
        self.mid = None
        self.last = None
        self.prev = None
        def traverse(root):
            if not root:
                return
            
            traverse(root.left)
            if self.prev:
                if self.prev.val > root.val:
                    if not self.fst:
                        self.fst = self.prev
                        self.mid = root
                    else:
                        self.last = root

            self.prev = root
            traverse(root.right)
        traverse(root)
        if self.last:
            self.last.val, self.fst.val = self.fst.val, self.last.val
        else:
            self.fst.val,self.mid.val = self.mid.val, self.fst.val
def main():
    # -------------------------
    # WRITE YOUR LOGIC BELOW
    # -------------------------
    
    return 0

if __name__ == "__main__":
    # Note: These prints will go to output.txt if USE_FILE is True
    main()