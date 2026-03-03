import sys
import os
from pathlib import Path
from typing  import Optional, List
from collections import defaultdict

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
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        out = []
        def traverse(root, col,row):
            if not root:
                return
            
            out.append([col,row, root.val])
            traverse(root.left, col-1, row+1)
            traverse(root.right, col+1, row+1)
        traverse(root, 0, 0)
        out.sort()
        outmap = defaultdict(list)
        for col, row, val in out:
            outmap[col].append(val)
        
        return list(outmap.values())


def main():
    # -------------------------
    # WRITE YOUR LOGIC BELOW
    # -------------------------
    
    return 0

if __name__ == "__main__":
    # Note: These prints will go to output.txt if USE_FILE is True
    main()