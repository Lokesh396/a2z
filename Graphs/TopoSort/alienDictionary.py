import sys
import os
from pathlib import Path
from typing import List
from collections import defaultdict

# Fast I/O and Recursion Setup
sys.setrecursionlimit(2000)
input = sys.stdin.readline

USE_FILE = True

if USE_FILE:
    BASE_DIR = Path(__file__).resolve().parents[2]
    sys.stdin = open(os.path.join(BASE_DIR, "input.txt"), "r")
    sys.stdout = open(os.path.join(BASE_DIR, "output.txt"), "w")

def foreignDictionary(self, dictionary: List[str]) -> str:
    """
    Pattern: Topological Sort (Graph Construction from Constraints)
    Difficulty: Hard
    Key Insight: Extract character ordering by comparing adjacent words letter-by-letter, build a DAG, then topo-sort; if word1 is a longer prefix of word2, ordering is invalid.
    Related: courseScheduleII.py, eventualSafeNodes.py
    """
    n = len(dictionary)
    letterSet = set()
    for word in dictionary:
        for letter in word:
            letterSet.add(letter)
    
    adjList = defaultdict(list)
    def buildGraph(word1, word2):
        m = min(len(word1), len(word2))
        for i in range(m):
            if word1[i] != word2[i]:
                adjList[word1[i]].append(word2[i])
                return True
        
        if len(word1) > len(word2):
            return False
        
        return True

    
    for i in range(n-1):
        if not buildGraph(dictionary[i], dictionary[i+1]):
            return ''
    def dfs(node, visit, path, order):
        if node in path:
            return False
        
        if node in visit:
            return True
        
        visit.add(node)
        path.add(node)

        for child in adjList[node]:
            if not dfs(child, visit, path, order):
                return False
        path.remove(node)
        order.append(node)

        return True
    visit = set()
    path = set()
    order = []
    for letter in letterSet:
        if letter not in visit:
            if not dfs(letter,visit, path, order):
                return ""
    return "".join(reversed(order))

def main():
    # -------------------------
    # WRITE YOUR LOGIC BELOW
    # -------------------------
    
    return 0

if __name__ == "__main__":
    # Note: These prints will go to output.txt if USE_FILE is True
    main()