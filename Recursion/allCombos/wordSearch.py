import sys
import os
from pathlib import Path
from typing import List

# Fast I/O and Recursion Setup
sys.setrecursionlimit(2000)
input = sys.stdin.readline

USE_FILE = True

if USE_FILE:
    BASE_DIR = Path(__file__).resolve().parents[2]
    sys.stdin = open(os.path.join(BASE_DIR, "input.txt"), "r")
    sys.stdout = open(os.path.join(BASE_DIR, "output.txt"), "w")

def search(board,i,j,visited, m, n,word,idx):
    if idx == len(word):
        return True
    if i < 0 or j < 0 or i >=m or j >= n:
        return False
    
    if not word[idx] == board[i][j] or (i,j) in visited:
        return False
    
    visited.add((i,j))

    left = search(board, i, j-1, visited, m, n, word, idx+1)
    right = search(board, i, j+1, visited, m, n, word, idx+1)
    top = search(board, i-1, j, visited, m, n, word, idx+1)
    bottom = search(board, i+1, j, visited, m, n, word, idx+1)

    visited.remove((i, j))

    return left or right or top or bottom

def exist( board: List[List[str]], word: str) -> bool:
    m = len(board)
    n = len(board[0])
    for i in range(m):
        for j in range(n):
            if search(board, i, j, set(),m,n,word,0):
                return True
    
    return False

def main():
    # -------------------------
    # WRITE YOUR LOGIC BELOW
    # -------------------------
    
    return 0

if __name__ == "__main__":
    # Note: These prints will go to output.txt if USE_FILE is True
    main()