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
    def Traversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        preorder = []
        postorder = []
        inorder = []
        stack = [[root, 1]]

        while stack:
            top = stack[-1]
            if top[1] == 1:
                preorder.append(top[0].val)
                stack[-1][1] += 1
                if top[0].left:
                    stack.append([top[0].left,1])
            elif top[1] == 2:
                inorder.append(top[0].val)
                stack[-1][1] += 1
                if top[0].right:
                    stack.append([top[0].right, 1])
            else:
                postorder.append(top[0].val)
                stack.pop()
        
        return postorder
    
def main():
    # -------------------------
    # WRITE YOUR LOGIC BELOW
    # -------------------------
    
    return 0

if __name__ == "__main__":
    # Note: These prints will go to output.txt if USE_FILE is True
    main()