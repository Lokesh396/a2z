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

    def __init__(self, val,prev=None,next=None):
        self.prev = prev
        self.val = val
        self.next = next
        
    def __repr__(self):
        prev_val = self.prev.val if self.prev else None
        next_val = self.next.val if self.next else None
        return f'Node(prev={prev_val}, val={self.val}, next={next_val})'


class LinkedList:
    def __init__(self):
        self.cnt = 0
        self.head = None
        self.tail = None
    
    def append(self, val):
        if not self.head:
            node = Node(val=val)
            self.head = node
            self.tail = node
            self.cnt += 1
            return
        node = Node(val, self.tail)
        self.tail.next = node
        self.tail = node
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

    def delete(self, nodeVal: int):
        if not self.head:
            return

        # delete head
        if self.head.val == nodeVal:
            if self.head == self.tail:
                self.head = None
                self.tail = None
            else:
                self.head = self.head.next
                self.head.prev = None
            self.cnt -= 1
            return

        temp = self.head
        while temp and temp.next:
            if temp.next.val == nodeVal:
                if temp.next == self.tail:
                    self.tail = temp
                    temp.next = None
                else:
                    temp.next = temp.next.next
                    temp.next.prev = temp
                self.cnt -= 1
                return
            temp = temp.next

        
    def reverse(self):
        curr = self.head

        self.head, self.tail = self.tail, self.head

        while curr:
            nxt = curr.next
            curr.next, curr.prev = curr.prev , curr.next
            curr = nxt
        
            


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
    linkedList.reverse()
    linkedList.traversal()
    linkedList.delete(3)
    linkedList.traversal()
    print("2 exists:",linkedList.isExists(2))
    return 0

if __name__ == "__main__":
    # Note: These prints will go to output.txt if USE_FILE is True
    main()