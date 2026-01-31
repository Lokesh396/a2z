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

class Stack():

    def __init__(self):
        self.stack = []
    
    def isEmpty(self) -> bool:
        return len(self.stack) == 0

    def top(self) ->int:
        if self.stack:
            return self.stack[-1]

        return -1

    def push(self, val:int):
        self.stack.append(val)
    
    def pop(self) -> int:
        if self.stack:
            return self.stack.pop()

        return -1

def main():
    # -------------------------
    # WRITE YOUR LOGIC BELOW
    # -------------------------
    stack = Stack()
    print(stack.isEmpty())
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    print(stack.stack)
    print(stack.top())
    print(stack.pop())
    print(stack.stack)
    return 0

if __name__ == "__main__":
    # Note: These prints will go to output.txt if USE_FILE is True
    main()