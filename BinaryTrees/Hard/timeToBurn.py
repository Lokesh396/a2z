import sys
import os
from pathlib import Path
from collections import deque
# Fast I/O and Recursion Setup
sys.setrecursionlimit(2000)
input = sys.stdin.readline

USE_FILE = True

if USE_FILE:
    BASE_DIR = Path(__file__).resolve().parents[2]
    sys.stdin = open(os.path.join(BASE_DIR, "input.txt"), "r")
    sys.stdout = open(os.path.join(BASE_DIR, "output.txt"), "w")
class BinaryTreeNode :
	def __init__(self, data) :
		self.data = data
		self.left = None
		self.right = None



def timeToBurnTree(root, start):

    # Write your code here.
    if not root:
        return 0

    hashmap = dict()

    q = deque()
    q.append(root)
    knode = None
    startNode = None
    while q:

        size = len(q)

        for i in range(size):
            node = q.popleft()
            if node.data == start:
                startNode = node
            if node.left:
                hashmap[node.left] = node
                q.append(node.left)
            if node.right:
                hashmap[node.right] = node
                q.append(node.right)
    out = [0]
    visited = set()
    def dfs(root, d):
        if not root:
            return 
        if root not in visited:
            visited.add(root)
        else:
            return

        out[0] = max(d, out[0])


        dfs(root.left, d+1)
        dfs(root.right, d+1)
        if root in hashmap:
            dfs(hashmap[root], d+1)
    dfs(startNode, 0)
    return out[0]
def main():
    # -------------------------
    # WRITE YOUR LOGIC BELOW
    # -------------------------
    
    return 0

if __name__ == "__main__":
    # Note: These prints will go to output.txt if USE_FILE is True
    main()