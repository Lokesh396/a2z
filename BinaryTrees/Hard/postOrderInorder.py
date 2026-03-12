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
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        

        self.post_index = len(inorder)-1
        inorder_map = {val:idx for idx, val in enumerate(inorder)}
        def helper(left, right):
            if left > right:
                return
            root_val = postorder[self.post_index]
            self.post_index -= 1
            root = TreeNode(root_val)
            in_index = inorder_map[root_val]
            root.right = helper(in_index+1, right)
            root.left = helper(left, in_index-1)

            return root
        
        return helper(0, len(inorder)-1)
def main():
    # -------------------------
    # WRITE YOUR LOGIC BELOW
    # -------------------------
    
    return 0

if __name__ == "__main__":
    # Note: These prints will go to output.txt if USE_FILE is True
    main()