# Linked Lists - Hard

Concise revision notes for the problems in this folder.

## Rotate Linked List (`RotateLL.py`)
Rotate the list to the right by k places.
Example:
Input: 1 -> 2 -> 3 -> 4 -> 5, k=2
Output: 4 -> 5 -> 1 -> 2 -> 3
Approach:
- Brute: rotate one step at a time. O(n*k).
- Optimal: make list circular, break at new head. O(n).

## Reverse Nodes in K Groups (`reverseNodesKGroups.py`)
Reverse nodes in groups of size k.
Example:
Input: 1 -> 2 -> 3 -> 4 -> 5, k=3
Output: 3 -> 2 -> 1 -> 4 -> 5
Approach:
- Brute: convert to array, reverse in chunks, rebuild. O(n) space.
- Optimal: in-place group reversal. O(n).

## Flatten a Linked List (`flattenaLL.py`)
Flatten a multi-level linked list into a single sorted list.
Example:
Input: 5 -> 10 -> 19 -> 28 (with bottom lists)
Output: 5 -> 7 -> 8 -> 10 -> 19 -> 20 -> 22 -> 28 -> 30 -> 50
Approach:
- Brute: collect all nodes, sort, rebuild. O(n log n).
- Optimal: merge lists iteratively or recursively. O(n log k).

## Clone Linked List with Random Pointer (`cloneLinkedList.py`)
Deep copy a list with next and random pointers.
Example:
Input: 1 -> 2 -> 3 with randoms (1->3, 2->1, 3->2)
Output: cloned list with same structure
Approach:
- Brute: hashmap from original to clone. O(n) space.
- Optimal: interleave nodes, set randoms, split. O(1) space.
