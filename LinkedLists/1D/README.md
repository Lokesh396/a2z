# Linked Lists - 1D

Concise revision notes for the problems in this folder.

## Delete Node in Linked List (`deleteNode.py`)
Delete a given node when head is not provided.
Example:
Input: 1 -> 2 -> 3 -> 4, delete node with value 3
Output: 1 -> 2 -> 4
Approach:
- Brute: if head known, traverse to prev and delete. O(n).
- Optimal: copy next node data into current, bypass next. O(1).

## Singly Linked List Basics (`linkedList.py`)
Implement basic operations: insert, delete, traverse.
Example:
Input: insert 1, insert 2, delete 1
Output: 2
Approach:
- Brute: N/A (core operations).
- Optimal: maintain head/tail for O(1) inserts where possible.
