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

class Queue:

    def __init__(self):
        self.queue = []
    
    def push(self, val) ->int:
        self.queue.append(val)
    
    def pop(self)->int:
        if self.queue:
            return self.queue.pop(0)
        return -1

    def isEmpty(self) -> bool:
        return len(self.queue) == 0

    def peek(self)->int:
        if self.queue:
            return self.queue[0]

        return -1

def main():
    # -------------------------
    # WRITE YOUR LOGIC BELOW
    # -------------------------
    queue = Queue()
    print(queue.isEmpty())
    queue.push(1)
    queue.push(2)
    queue.push(3)
    queue.push(4)
    print(queue.queue)
    print(queue.peek())
    print(queue.pop())
    print(queue.queue)
    return 0

if __name__ == "__main__":
    # Note: These prints will go to output.txt if USE_FILE is True
    main()