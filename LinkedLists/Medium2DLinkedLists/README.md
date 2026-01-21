# Linked Lists - Medium 2D

Concise revision notes for the problems in this folder.

## Find Pairs with Given Sum (`findPairs.py`)
Find pairs of nodes from a doubly linked list that sum to target.
Example:
Input: 1 <-> 2 <-> 4 <-> 5, target=6
Output: (1,5), (2,4)
Approach:
- Brute: check all pairs. O(n^2).
- Optimal: two pointers from both ends. O(n).

## Remove Duplicates (Unsorted) (`removeDuplicates.py`)
Remove duplicate nodes from an unsorted doubly linked list.
Example:
Input: 1 <-> 2 <-> 1 <-> 3
Output: 1 <-> 2 <-> 3
Approach:
- Brute: nested scan for each node. O(n^2).
- Optimal: hash set of seen values. O(n) space.

## Remove Duplicates in Sorted (`removeDuplicatesinSorted.py`)
Remove duplicates from a sorted doubly linked list.
Example:
Input: 1 <-> 1 <-> 2 <-> 2 <-> 3
Output: 1 <-> 2 <-> 3
Approach:
- Brute: N/A (single pass already optimal).
- Optimal: skip duplicates while traversing. O(n).

## Reverse Nodes in K Groups (`reverseNodesKGroups.py`)
Reverse nodes in groups of size k.
Example:
Input: 1 <-> 2 <-> 3 <-> 4 <-> 5, k=2
Output: 2 <-> 1 <-> 4 <-> 3 <-> 5
Approach:
- Brute: convert to array, reverse in chunks, rebuild. O(n) space.
- Optimal: in-place reversal per group. O(n).
