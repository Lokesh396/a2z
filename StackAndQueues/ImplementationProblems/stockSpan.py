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

class StockSpanner:

    def __init__(self):
        self.stack = []
        self.day = 0

    def next(self, price: int) -> int:
        while self.stack and self.stack[-1][0] <= price:
            self.stack.pop()
        ans = 1
        if self.stack:
            ans = (self.day+1) - self.stack[-1][1]
        else:
            ans = self.day + 1
        
        self.day += 1
        self.stack.append([price, self.day])
        return ans

        
        



def main():
    # -------------------------
    # WRITE YOUR LOGIC BELOW
    # -------------------------
    
    # Your StockSpanner object will be instantiated and called as such:
    obj = StockSpanner()
    n = int(input())
    for i in range(n):
        print(obj.next(int(input())))

if __name__ == "__main__":
    # Note: These prints will go to output.txt if USE_FILE is True
    main()