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

'''

    Following is the Binary Tree node structure
    
    class BinaryTreeNode:
        def __init__(self, data):
            self.data = data
            self.left = None
            self.right = None

'''
        
def changeTree(root): 
    # Write your code here.
    

    def dfs(root):
        if not root:
            return 
        
        leftval = root.left.data if root.left else 0
        rightval = root.right.data if root.right else 0
        if leftval + rightval < root.data:
            if root.left:
                root.left.data = root.data
            if root.right:
                root.right.data = root.data
        else:
            root.data = leftval + rightval
        dfs(root.left)
        dfs(root.right)

        leftval = root.left.data if root.left else 0
        rightval = root.right.data if root.right else 0
        root.data = max(leftval + rightval, root.data)
    
    dfs(root)

def main():
    # -------------------------
    # WRITE YOUR LOGIC BELOW
    # -------------------------
    
    return 0

if __name__ == "__main__":
    # Note: These prints will go to output.txt if USE_FILE is True
    main()