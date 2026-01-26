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

    
        

def solveSudoku( board: List[List[str]]) -> None:
    """
    Do not return anything, modify board in-place instead.
    """
    row = [set() for _ in range(9)]
    col = [set() for _ in range(9)]
    box = [set() for _ in range(9)]
    for i in range(9):
        for j in range(9):
            if board[i][j] != '.':
                val = board[i][j]
                row[i].add(val)
                col[j].add(val)
                box_id = (i//3)*3 + j//3
                box[box_id].add(val)
    def generate( board, i, j):
        if i == 9:
            return True
        
        if j == 9:
            return generate(board, i+1, 0)
        
        if board[i][j] != '.':
            return generate(board, i, j+1)
        
    
        for k in range(1,10):
            boxid = (i//3)*3+j//3
            val = f'{k}'
            if val not in row[i] and val not in col[j] and val not in box[boxid]:
                board[i][j] = val
                row[i].add(val)
                col[j].add(val)
                box[boxid].add(val)

                if generate(board,i, j+1):
                    return True
                
                board[i][j]='.'
                row[i].remove(val)
                col[j].remove(val)
                box[boxid].remove(val)
    generate(board, 0, 0)
def main():
    # -------------------------
    # WRITE YOUR LOGIC BELOW
    # -------------------------
    board = [['.'] * 9 for _ in range(9)]
    solveSudoku(board=board)
    print(*board)
    return 0

if __name__ == "__main__":
    # Note: These prints will go to output.txt if USE_FILE is True
    main()