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

    def __init__(self, val,next=None):
        self.val = val
        self.next = next
        

class LinkedList:
    def __init__(self):
        self.cnt = 0
        self.head = None
    
    def append(self, val):
        if not self.head:
            self.head = Node(val=val)
            self.cnt += 1
            return
        temp = self.head

        while temp.next:
            temp = temp.next
        temp.next = Node(val=val)
        self.cnt += 1


    def traversal(self):
        temp = self.head

        while temp:
            print(temp.val, end=' -> ')
            temp = temp.next
        print('\n')
        return
    
    def __len__(self):

        return self.cnt

    def delete(self, nodeVal:int):
        if self.head and  self.head.val == nodeVal:
            self.head = self.head.next
            self.cnt -= 1
            return
        temp = self.head
        while temp and temp.next:
            if temp.next.val == nodeVal:
                temp.next = temp.next.next
                self.cnt -= 1
                return
            temp = temp.next
    
    def isExists(self,nodeVal:int):

        temp = self.head
        while temp:
            if temp.val == nodeVal:
                return True
            temp = temp.next
        
        return False

def main():
    # -------------------------
    # WRITE YOUR LOGIC BELOW
    # -------------------------
    linkedList = LinkedList()
    linkedList.append(1)
    linkedList.append(2)
    linkedList.append(3)
    print(len(linkedList))
    linkedList.traversal()
    linkedList.delete(3)
    linkedList.traversal()
    print("2 exists:",linkedList.isExists(2))
    return 0

if __name__ == "__main__":
    # Note: These prints will go to output.txt if USE_FILE is True
    main()