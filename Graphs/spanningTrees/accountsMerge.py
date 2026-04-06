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

def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
    n = len(accounts)
    parent =  [i for i in range(n)]
    rank = [0 for _ in range(n)]

    def findulp(node):
        if parent[node] == node:
            return node
        
        parent[node] = findulp(parent[node])
        return parent[node]
    
    def unionbyrank(u, v):
        up_u = findulp(u)
        up_v = findulp(v)

        if rank[up_u] < rank[up_v]:
            parent[up_u] = up_v
        elif rank[up_v] < rank[up_u]:
            parent[up_v] = up_u
        else:
            parent[up_v] = up_u
            rank[up_u] += 1
    mailnodemap = {}
    for i in range(n):
        for j in range(1, len(accounts[i])):
            mail = accounts[i][j]
            if mail not in mailnodemap:
                mailnodemap[mail] = i
            else:
                unionbyrank(i, mailnodemap[mail])
    
    mergedmail = [[] for i in range(n)]

    for mail, idx in mailnodemap.items():
        node = findulp(idx)
        mergedmail[node].append(mail)
    
    ans = []

    for i in range(n):
        if not mergedmail[i]:
            continue
        
        temp = [accounts[i][0]]
        mergedmail[i].sort()
        for mail in mergedmail[i]:
            temp.append(mail)
        ans.append(temp[::])

    return ans
def main():
    # -------------------------
    # WRITE YOUR LOGIC BELOW
    # -------------------------
    
    return 0

if __name__ == "__main__":
    # Note: These prints will go to output.txt if USE_FILE is True
    main()