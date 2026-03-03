import sys
import os
from pathlib import Path
from typing import List
from collections import defaultdict, deque

# Fast I/O and Recursion Setup
sys.setrecursionlimit(2000)
input = sys.stdin.readline

USE_FILE = True

if USE_FILE:
    BASE_DIR = Path(__file__).resolve().parents[2]
    sys.stdin = open(os.path.join(BASE_DIR, "input.txt"), "r")
    sys.stdout = open(os.path.join(BASE_DIR, "output.txt"), "w")

# Following is the TreeNode class structure.
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def bottomView(root: BinaryTreeNode) -> List[int]:
    # Write your code here.
    if not root:
        return []
    q = deque()

    q.append((root, 0))
    colmap = defaultdict(int)
    while q:

        size = len(q)

        for i in range(size):
            node = q.popleft()
            colmap[node[1]] = node[0].data

            
            if node[0].left:
                q.append([node[0].left, node[1]-1])
            if node[0].right:
                q.append([node[0].right,node[1]+ 1])
    
    colmap = sorted(colmap.items())
    return [v for k, v in colmap]
def main():
    # -------------------------
    # WRITE YOUR LOGIC BELOW
    # -------------------------
    
    return 0

if __name__ == "__main__":
    # Note: These prints will go to output.txt if USE_FILE is True
    main()