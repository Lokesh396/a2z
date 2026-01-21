# Arrays - Hard

Concise revision notes for the problems in this folder.

## 3Sum (`threeSum.py`)
Find all unique triplets that sum to 0.
Example:
Input: [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Approach:
- Brute: 3 nested loops + set. O(n^3).
- Optimal: sort + two pointers per i. O(n^2).

## 4Sum (`fourSum.py`)
Find all unique quadruplets that sum to target.
Example:
Input: [1,0,-1,0,-2,2], target=0
Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
Approach:
- Brute: 4 nested loops + set. O(n^4).
- Optimal: sort + two pointers inside two loops. O(n^3).

## Majority Element II (> n/3) (`majorityElement2.py`)
Find all elements appearing more than n/3 times.
Example:
Input: [3,2,3]
Output: [3]
Approach:
- Brute: frequency map. O(n) space.
- Optimal: Boyer-Moore (two candidates). O(n), O(1) space.

## Pascal's Triangle (`PascalsTriangle.py`)
Generate the first n rows of Pascal's Triangle.
Example:
Input: n=5
Output:
[ [1],
  [1,1],
  [1,2,1],
  [1,3,3,1],
  [1,4,6,4,1] ]
Approach:
- Brute: compute nCk via factorial. O(n^3) naive.
- Optimal: build rows from previous row. O(n^2).

## Largest Subarray With Zero Sum (`LargestSubarrayWirhZerosum.py`)
Return the length of the longest subarray with sum 0.
Example:
Input: [9,-3,3,-1,6,-5]
Output: 5
Approach:
- Brute: all subarrays. O(n^2).
- Optimal: prefix sum first occurrence map. O(n).

## Count Subarrays With XOR K (`numberOfSubarrayswithxork.py`)
Count subarrays with xor equal to K.
Example:
Input: [4,2,2,6,4], K=6
Output: 4
Approach:
- Brute: all subarrays. O(n^2).
- Optimal: prefix xor + hashmap counts. O(n).

## Merge Intervals (`mergeIntervals.py`)
Merge all overlapping intervals.
Example:
Input: [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Approach:
- Brute: compare and merge repeatedly. O(n^2).
- Optimal: sort by start, then merge in one pass. O(n log n).

## Merge Two Sorted Arrays In-Place (`mergeSortedArrays.py`)
Merge two sorted arrays without extra space (when possible).
Example:
Input: arr1=[1,3,5], arr2=[2,4,6]
Output: arr1=[1,2,3], arr2=[4,5,6]
Approach:
- Brute: extra array then split. O(n+m) space.
- Optimal: gap method or two-pointer swap + sort. O((n+m) log (n+m)) or better.

## Repeating and Missing Number (`repeatingMissingNumber.py`)
Find the repeating and the missing number in 1..n.
Example:
Input: [3,1,2,5,3]
Output: repeating=3, missing=4
Approach:
- Brute: count frequencies. O(n) space.
- Optimal: math (sum, sum of squares) or xor. O(n), O(1) space.

## Count Inversions (`countInversions.py`)
Count pairs (i,j) with i<j and a[i] > a[j].
Example:
Input: [2,4,1,3,5]
Output: 3
Approach:
- Brute: check all pairs. O(n^2).
- Optimal: merge sort based counting. O(n log n).

## Reverse Pairs (`reversePairs.py`)
Count pairs (i,j) with i<j and a[i] > 2*a[j].
Example:
Input: [1,3,2,3,1]
Output: 2
Approach:
- Brute: check all pairs. O(n^2).
- Optimal: merge sort with two-pointer count. O(n log n).

## Maximum Product Subarray (`maximumProductSubarray.py`)
Find maximum product of a contiguous subarray.
Example:
Input: [2,3,-2,4]
Output: 6
Approach:
- Brute: all subarrays. O(n^2).
- Optimal: track max and min product ending here. O(n).
