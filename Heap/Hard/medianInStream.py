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
from heapq import heappush, heappop
class MedianFinder:

    def __init__(self):
        self.maxheap = []
        self.minheap = []

    def addNum(self, num: int) -> None:
        heappush(self.maxheap, -num)

        if self.minheap and self.maxheap and -self.maxheap[0] > self.minheap[0]:
            heappush(self.minheap,-heappop(self.maxheap))
        
        if len(self.maxheap) > len(self.minheap) +1 :
            heappush(self.minheap, -heappop(self.maxheap))
        
        if len(self.minheap) > len(self.maxheap)+1:
            heappush(self.maxheap, -heappop(self.minheap))


    def findMedian(self) -> float:
        if len(self.minheap) > len(self.maxheap):
            return self.minheap[0]
        
        elif len(self.maxheap) > len(self.minheap):
            return -self.maxheap[0]
        
        else:
            return ((self.minheap[0] + (-self.maxheap[0]))/2.0)

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
def main():
    # -------------------------
    # WRITE YOUR LOGIC BELOW
    # -------------------------
    
    return 0

if __name__ == "__main__":
    # Note: These prints will go to output.txt if USE_FILE is True
    main()