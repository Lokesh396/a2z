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
    ------- Binary Tree node structure -------
            class   BinaryTreeNode :
                def __init__(self, data) :
                    self.data = data
                    self.left = None
                    self.right = None

                def __del__(self):
                    if self.left:
                        del self.left
                    if self.right:
                        del self.right
      
'''
def predecessorSuccessor(root, key):

	# Write your code here.
    if not root:
        return [-1, -1]
    stack = []
    inorder = []
    while True:
        if root:
            stack.append(root)
            root = root.left
        else:
            if not stack:
                break
            
            root = stack.pop()
            inorder.append(root.data)
            root = root.right
    
    ans = []
    for idx, val in enumerate(inorder):
        if val >= key:
            if idx >0 :
                ans.append(inorder[idx-1])
            else:
                ans.append(-1)
            
            if inorder[idx] == key:
                if idx < len(inorder)-1:
                    ans.append(inorder[idx+1])
                else:
                    ans.append(-1)
            else:
                if idx < len(inorder):
                    ans.append(inorder[idx])
                else:
                    ans.append(-1)
            return ans

    return [inorder[-1], -1]


def predecessorSuccessorV1(root, key):
    pre = -1
    suc = -1

    while root:
        if root.data > key:
            suc = root.data
            root = root.left
        elif root.data < key:
            pre = root.data
            root = root.right
        else:
            temp = root.left
            while temp:
                pre = temp.data
                temp = temp.right
            
            temp = root.right

            while temp:
                suc = temp.data
                temp = temp.left
    return [pre, suc]

def main():
    # -------------------------
    # WRITE YOUR LOGIC BELOW
    # -------------------------
    
    return 0

if __name__ == "__main__":
    # Note: These prints will go to output.txt if USE_FILE is True
    main()