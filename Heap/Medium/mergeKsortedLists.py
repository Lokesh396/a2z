import sys
import os
from pathlib import Path
from typing import List, Optional
import heapq

# Fast I/O and Recursion Setup
sys.setrecursionlimit(2000)
input = sys.stdin.readline

USE_FILE = True

if USE_FILE:
    BASE_DIR = Path(__file__).resolve().parents[2]
    sys.stdin = open(os.path.join(BASE_DIR, "input.txt"), "r")
    sys.stdout = open(os.path.join(BASE_DIR, "output.txt"), "w")

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeKLists(lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        temphead = ListNode(-1)
        dummy = temphead
        out = []
        cnt = 0
        for head in lists:
            while head:
                cnt += 1
                heapq.heappush(out, [head.val,cnt, head])
                head = head.next

        while out:
            node = heapq.heappop(out)
            dummy.next = node[2]
            dummy = dummy.next
        
        return temphead.next

def mergeKListsv2(lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []

        for idx, node in enumerate(lists):
            if node:
                heapq.heappush(heap, [node.val, idx, node])
        
        dummyhead = ListNode(-1)
        dummy = dummyhead

        while heap:
            val, idx, node = heapq.heappop(heap)
            dummy.next = node
            dummy = dummy.next

            if node.next:
                heapq.heappush(heap, [node.next.val, idx, node.next])
        
        return dummyhead.next

def main():
    # -------------------------
    # WRITE YOUR LOGIC BELOW
    # -------------------------
    
    return 0

if __name__ == "__main__":
    # Note: These prints will go to output.txt if USE_FILE is True
    main()