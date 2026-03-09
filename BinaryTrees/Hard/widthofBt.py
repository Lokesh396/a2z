import sys
import os
from pathlib import Path
from typing import Optional
from collections import deque

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
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        q = deque()
        q.append((root, 0))
        max_len = 0
        while q:
            size = len(q)
            last = 0
            fst = 0
            min_index = q[0][1]
            for i in range(size):
                node,idx = q.popleft()
                curr_index = idx - min_index
                if i == 0:
                    fst = curr_index
                if i == size-1:
                    last = curr_index
                if node.left:
                    q.append((node.left,2*curr_index+1))
                
                if node.right:
                    q.append((node.right,2*curr_index+2))

            max_len = max(max_len, last-fst+1)

        return max_len

def main():
    # -------------------------
    # WRITE YOUR LOGIC BELOW
    # -------------------------
    
    return 0

if __name__ == "__main__":
    # Note: These prints will go to output.txt if USE_FILE is True
    main()