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

def ladderLength( beginWord: str, endWord: str, wordList: List[str]) -> int:
    """
    Pattern: BFS / Shortest Path (Word Graph)
    Difficulty: Hard
    Key Insight: Model as unweighted graph where edges connect words differing by one letter; BFS guarantees the fewest transformations.
    Related: rottingOranges.py, matrix01.py
    """
    wordset = set(wordList)

    q = deque()
    q.append((beginWord, 1))
    if beginWord in wordset:
        wordset.remove(beginWord)
    while q:
        word, steps = q.popleft()
        if word == endWord:
            return steps
        
        wordl = list(word)
        for i in range(len(wordl)):
            original = wordl[i]
            
            for j in range(26):
                wordl[i] = chr(97 + j)
                newword = "".join(wordl)
                if newword in wordset:
                    wordset.remove(newword)
                    q.append((newword, steps+1))
            wordl[i] = original
    
    return 0
def main():
    # -------------------------
    # WRITE YOUR LOGIC BELOW
    # -------------------------
    
    return 0

if __name__ == "__main__":
    # Note: These prints will go to output.txt if USE_FILE is True
    main()