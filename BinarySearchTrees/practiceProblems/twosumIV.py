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
class BSTIterator:

    def __init__(self, root: Optional[TreeNode], reverse):
        self.root = root
        self.stack = []
        self.reverse = reverse
        self.pushall(root)
    def pushall(self,node):
        while node:
            self.stack.append(node)
            if self.reverse:
                node = node.right
            else:
                node = node.left

    def next(self) -> int:
        temp = self.stack.pop()
        if self.reverse:
            self.pushall(temp.left)
        else:
            self.pushall(temp.right)
        return temp.val 

    def hasNext(self) -> bool:
       return len(self.stack) > 0
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        left = BSTIterator(root, False)
        right = BSTIterator(root, True)

        
        l = left.next()
        r = right.next()
        print(l,r)
        while l < r:
            sm = l +r
            if sm == k:
                return True
            elif sm > k:
                r = right.next()
            else:
                l = left.next()
        
        return False
def main():
    # -------------------------
    # WRITE YOUR LOGIC BELOW
    # -------------------------
    
    return 0

if __name__ == "__main__":
    # Note: These prints will go to output.txt if USE_FILE is True
    main()