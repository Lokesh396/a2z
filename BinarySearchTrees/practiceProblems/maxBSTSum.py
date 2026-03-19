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
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        
        ans = [0]
        def traverse(node):
            if not node:
                #       ans,min,        max,           isbst
                return [0, float('inf'), -float('inf'), True]
            
            l = traverse(node.left)
            r = traverse(node.right)

            if l[3] and r[3] and l[2] < node.val and node.val < r[1]:

                csum = l[0] + r[0] + node.val
                ans[0]= max(ans[0], csum)

                mn = min(l[1],node.val)
                mx = min(r[2], node.val)

                return [csum, mn, mx, True]
            else:
                return [0,float('inf'), -float('inf'), False]
        
        traverse(root)
        return ans[0]

def main():
    # -------------------------
    # WRITE YOUR LOGIC BELOW
    # -------------------------
    
    return 0

if __name__ == "__main__":
    # Note: These prints will go to output.txt if USE_FILE is True
    main()