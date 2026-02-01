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
    def __init__(self, value):
        self.data = value  # storing the incoming value passed by user in the data property
        self.next = None
class Queue:
    def __init__(self):
        # Create an instance of the LinkedList
        self.head = None
        self.tail = None

    def enqueue(self, data):
        # Add element to the tail of the list (enqueue)
        node = Node(data)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node

    def is_empty(self):
        # Check if the queue is empty
        return self.head is None

    def dequeue(self):
        # If the queue is empty, return -1
        # Remove element from the head (dequeue)
        if self.head is None:
            return -1

        elif self.head == self.tail:
            data = self.head.data
            self.head = None
            self.tail = None
            return data
        else:
            data = self.head.data
            self.head = self.head.next
            return data

# Input and processing


def main():
    # -------------------------
    # WRITE YOUR LOGIC BELOW
    # -------------------------
    q = int(input())  # Read the number of queries
    queries = []

    # Read each query from the user
    for _ in range(q):
        query = list(map(int, input().split()))
        queries.append(query)

    # Create an instance of the Queue
    queue = Queue()

    output = []

    # Process each query
    for query in queries:
        if query[0] == 1:  # Enqueue operation
            queue.enqueue(query[1])
        elif query[0] == 2:  # Dequeue operation
            result = queue.dequeue()
            output.append(str(result))  # Store the result of dequeue in the output list

    # Print the results of all type 2 queries (dequeues) in one line, space-separated
    print(" ".join(output))
    return 0

if __name__ == "__main__":
    # Note: These prints will go to output.txt if USE_FILE is True
    main()