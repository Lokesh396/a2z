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

class Node:

    def __init__(self, key, data):
        self.prev = None
        self.data = data
        self.key = key
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        
        self.cap = capacity
        self.head = None
        self.tail = None
        self.lookup = dict()
    
    def movehead(self, key):
        if key != self.head.key:
            temp = self.lookup[key]
            if temp == self.tail:
                self.tail = self.tail.prev
            temp.prev.next = temp.next
            if temp.next:
                temp.next.prev = temp.prev
            self.head.prev = temp
            temp.next = self.head
            self.head = temp
            temp.prev = None

    def get(self, key: int) -> int:
        if key not in self.lookup:
            return -1
        
        self.movehead(key)
        return self.lookup[key].data

    def put(self, key: int, value: int) -> None:
        if key in self.lookup:
            self.lookup[key].data = value
            self.movehead(key)
            return
        node = Node(key, value)
        self.lookup[key] = node
        if len(self.lookup) <= self.cap:
            if not self.head:
                self.head = node
                self.tail = node
            
        else:
            del self.lookup[self.tail.key]
            if self.head == self.tail:
                self.head = node
                self.tail = node
            else:
                self.tail = self.tail.prev
                self.tail.next = None
        self.head.prev = node
        node.next = self.head
        self.head = node
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

def main():
    # -------------------------
    # WRITE YOUR LOGIC BELOW
    # -------------------------
    
    return 0

if __name__ == "__main__":
    # Note: These prints will go to output.txt if USE_FILE is True
    main()