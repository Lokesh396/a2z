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

def inorder(root, ans):
    if not root:
        return
    inorder(root.left, ans)
    ans.append(root.val)
    inorder(root.right, ans)

def merge(arr1, arr2):
    i = 0
    j = 0
    out = []
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            out.append(arr1[i])
            i += 1
        else:
            out.append(arr2[j])
            j += 1
    
    while i < len(arr1):
        out.append(arr1[i])
        i += 1
    
    while j < len(arr2):
        out.append(arr2[i])
        j += 1
    
    return out

def main():
    # -------------------------
    # WRITE YOUR LOGIC BELOW
    # -------------------------
    root1 = None
    root2 = None
    ans1 = []
    inorder(root1)
    ans2 = []
    inorder(root2)
    return merge(arr1=ans1, arr2=ans2)
    return 0

if __name__ == "__main__":
    # Note: These prints will go to output.txt if USE_FILE is True
    main()