import sys
import os
from pathlib import Path
from collections import deque
from typing import List

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
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def distanceK(root: TreeNode, target: TreeNode, k: int) -> List[int]:
    if not root:
        return []
    if k == 0:
        return [target.val]
    hashmap = dict()

    q = deque()
    q.append(root)
    knode = None
    while q:

        size = len(q)

        for i in range(size):
            node = q.popleft()
            if node.left:
                hashmap[node.left] = node
                q.append(node.left)
            if node.right:
                hashmap[node.right] = node
                q.append(node.right)
    out = []
    visited = set()
    def dfs(root, d):
        if not root:
            return 
        if root not in visited:
            visited.add(root)
        else:
            return
        if d == k:
            out.append(root.val)
            return

        dfs(root.left, d+1)
        dfs(root.right, d+1)
        if root in hashmap:
            dfs(hashmap[root], d+1)
    dfs(target, 0)
    return out
def main():
    # -------------------------
    # WRITE YOUR LOGIC BELOW
    # -------------------------
    
    return 0

if __name__ == "__main__":
    # Note: These prints will go to output.txt if USE_FILE is True
    main()