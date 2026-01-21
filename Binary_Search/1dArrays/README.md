# Binary Search - 1D Arrays

Concise revision notes for the problems in this folder.

## Binary Search (`binarySearch.py`)
Find the index of target in a sorted array.
Example:
Input: arr=[1,3,5,7], target=5
Output: 2
Approach:
- Brute: linear scan. O(n).
- Optimal: classic binary search. O(log n).

## Insert Position (`insertPosition.py`)
Find index where target should be inserted in sorted array.
Example:
Input: [1,3,5,6], target=2
Output: 1
Approach:
- Brute: linear scan. O(n).
- Optimal: lower bound via binary search. O(log n).

## Ceil in Sorted Array (`ceilSArray.py`)
Smallest element >= target.
Example:
Input: [1,2,4,6], target=5
Output: 6
Approach:
- Brute: scan and track min >= target. O(n).
- Optimal: binary search for lower bound. O(log n).

## Upper Bound (`upperBound.py`)
First index with element > target.
Example:
Input: [1,2,2,3], target=2
Output: 3
Approach:
- Brute: scan until > target. O(n).
- Optimal: binary search. O(log n).

## Lower Bound (`lowerBound.py`)
First index with element >= target.
Example:
Input: [1,2,2,3], target=2
Output: 1
Approach:
- Brute: scan until >= target. O(n).
- Optimal: binary search. O(log n).

## Floor in Sorted Array (`floorSArray.py`)
Largest element <= target.
Example:
Input: [1,2,4,6], target=5
Output: 4
Approach:
- Brute: scan and track max <= target. O(n).
- Optimal: binary search for floor. O(log n).

## Count Occurrences (`occurences.py`)
Count total occurrences of target in sorted array.
Example:
Input: [1,2,2,2,3], target=2
Output: 3
Approach:
- Brute: scan and count. O(n).
- Optimal: upper bound - lower bound. O(log n).

## First and Last Occurrence (`firstandlastoccurence.py`)
Find first and last index of target.
Example:
Input: [1,2,2,2,3], target=2
Output: [1,3]
Approach:
- Brute: scan from both ends. O(n).
- Optimal: two binary searches. O(log n).

## Peak Element (`peakElement.py`)
Find any peak element (greater than neighbors).
Example:
Input: [1,2,3,1]
Output: index 2
Approach:
- Brute: scan and check neighbors. O(n).
- Optimal: binary search on slope. O(log n).

## Rotation Index in Sorted Array (`rotateIndex.py`)
Find index of minimum element in rotated sorted array.
Example:
Input: [4,5,6,7,0,1,2]
Output: 4
Approach:
- Brute: linear scan for min. O(n).
- Optimal: binary search on sorted halves. O(log n).

## Minimum in Rotated Sorted Array (`minimumSortedArray.py`)
Find the minimum element in rotated sorted array (with duplicates).
Example:
Input: [2,2,2,0,1]
Output: 0
Approach:
- Brute: linear scan for min. O(n).
- Optimal: binary search with duplicate handling. O(log n) average.

## Search in Rotated Sorted Array I (`searchRotatedSortedI.py`)
Search target in rotated array without duplicates.
Example:
Input: [4,5,6,7,0,1,2], target=0
Output: 4
Approach:
- Brute: linear scan. O(n).
- Optimal: binary search on sorted half. O(log n).

## Search in Rotated Sorted Array II (`searchRotatedSortedII.py`)
Search target in rotated array with duplicates.
Example:
Input: [2,5,6,0,0,1,2], target=0
Output: True
Approach:
- Brute: linear scan. O(n).
- Optimal: binary search with duplicate shrink. O(log n) average.

## Single Element in Sorted Array (`singleElement.py`)
Find the element that appears once when others appear twice.
Example:
Input: [1,1,2,3,3]
Output: 2
Approach:
- Brute: XOR all elements. O(n).
- Optimal: binary search on pair indices. O(log n).
