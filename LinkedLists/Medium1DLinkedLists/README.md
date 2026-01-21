# Linked Lists - Medium 1D

Concise revision notes for the problems in this folder.

## Add 1 to Linked List (`add1toLL.py`)
Treat list as a number and add 1.
Example:
Input: 1 -> 2 -> 9
Output: 1 -> 3 -> 0
Approach:
- Brute: convert to number, add, rebuild. O(n) space.
- Optimal: reverse list, add with carry, reverse back. O(n).

## Add Two Numbers (`add2numbers.py`)
Sum two numbers represented by linked lists.
Example:
Input: 2 -> 4 -> 3, 5 -> 6 -> 4
Output: 7 -> 0 -> 8
Approach:
- Brute: convert to ints, add, rebuild. O(n+m) space.
- Optimal: digit-wise addition with carry. O(n+m).

## Intersection of Y Linked Lists (`intersectionYLL.py`)
Find the intersection node of two linked lists.
Example:
Input: A=1->2->3->4, B=6->3->4 (intersect at 3)
Output: node with value 3
Approach:
- Brute: for each node in A, scan B. O(n*m).
- Optimal: two pointers switching heads. O(n+m).

## Detect Cycle (`loopLL.py`)
Check if a linked list has a cycle.
Example:
Input: 1 -> 2 -> 3 -> 4 -> 2 (cycle)
Output: True
Approach:
- Brute: hash set of visited nodes. O(n) space.
- Optimal: Floyd's cycle detection. O(1) space.

## Length of Cycle (`loopLength.py`)
Return the length of the cycle if it exists.
Example:
Input: 1 -> 2 -> 3 -> 4 -> 2
Output: 3
Approach:
- Brute: hash set and count when revisit. O(n) space.
- Optimal: Floyd's meeting point then count cycle length. O(1) space.

## Start of Cycle (`loopStartingPoint.py`)
Find the node where the cycle begins.
Example:
Input: 1 -> 2 -> 3 -> 4 -> 2
Output: node with value 2
Approach:
- Brute: hash set to find first repeated. O(n) space.
- Optimal: Floyd + reset one pointer to head. O(1) space.

## Middle of Linked List (`middleLL.py`)
Find the middle node.
Example:
Input: 1 -> 2 -> 3 -> 4 -> 5
Output: 3
Approach:
- Brute: count length then move n/2. O(n).
- Optimal: slow/fast pointers. O(n).

## Odd Even Linked List (`oddEvenPointer.py`)
Group odd indices together followed by even indices.
Example:
Input: 1 -> 2 -> 3 -> 4 -> 5
Output: 1 -> 3 -> 5 -> 2 -> 4
Approach:
- Brute: build two lists and join. O(n) space.
- Optimal: pointer rearrangement in-place. O(1) space.

## Palindrome Linked List (`palindromeLL.py`)
Check if linked list is a palindrome.
Example:
Input: 1 -> 2 -> 2 -> 1
Output: True
Approach:
- Brute: copy to array and check. O(n) space.
- Optimal: reverse second half and compare. O(1) space.

## Remove Middle Node (`removeMiddle.py`)
Delete the middle node of the list.
Example:
Input: 1 -> 2 -> 3 -> 4 -> 5
Output: 1 -> 2 -> 4 -> 5
Approach:
- Brute: count length then delete at n/2. O(n).
- Optimal: slow/fast with prev pointer. O(n).

## Remove Nth Node From End (`removeNNode.py`)
Remove the nth node from end.
Example:
Input: 1 -> 2 -> 3 -> 4 -> 5, n=2
Output: 1 -> 2 -> 3 -> 5
Approach:
- Brute: compute length then delete. O(n).
- Optimal: two pointers with gap n. O(n).

## Reverse Linked List (Iterative) (`reverseLLIterative.py`)
Reverse a singly linked list.
Example:
Input: 1 -> 2 -> 3
Output: 3 -> 2 -> 1
Approach:
- Brute: push to stack then rebuild. O(n) space.
- Optimal: iterative pointer reversal. O(n), O(1) space.

## Reverse Linked List (Recursive) (`reverseLLrecursive.py`)
Reverse a linked list using recursion.
Example:
Input: 1 -> 2 -> 3
Output: 3 -> 2 -> 1
Approach:
- Brute: use stack. O(n) space.
- Optimal: recursive reversal. O(n) time, O(n) stack.

## Sort 0s, 1s, 2s (`sort0s1s2s.py`)
Sort a list containing only 0,1,2.
Example:
Input: 2 -> 1 -> 0 -> 1
Output: 0 -> 1 -> 1 -> 2
Approach:
- Brute: count values then overwrite. O(n).
- Optimal: three dummy lists then merge. O(n).

## Sort Linked List (`sortLL.py`)
Sort a linked list in ascending order.
Example:
Input: 4 -> 2 -> 1 -> 3
Output: 1 -> 2 -> 3 -> 4
Approach:
- Brute: copy to array, sort, rebuild. O(n log n).
- Optimal: merge sort on list. O(n log n) time, O(log n) stack.
