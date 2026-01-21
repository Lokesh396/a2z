# Arrays - Medium

Concise revision notes for the problems in this folder.

## Leaders in an Array (`Leaders.py`)
Elements greater than all elements to their right.
Example:
Input: [16,17,4,3,5,2]
Output: [17,5,2]
Approach:
- Brute: for each i, scan right side. O(n^2).
- Optimal: traverse from right, track max. O(n).

## Sort 0s, 1s, 2s (`Sort012.py`)
Sort an array of 0s, 1s, and 2s.
Example:
Input: [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
Approach:
- Brute: counting sort. O(n).
- Optimal: Dutch National Flag (3 pointers). O(n), in-place.

## Buy and Sell Stock (Single Transaction) (`buyAndSellStock.py`)
Max profit from one buy and one sell.
Example:
Input: [7,1,5,3,6,4]
Output: 5
Approach:
- Brute: check all pairs. O(n^2).
- Optimal: track min price and max profit. O(n).

## Longest Consecutive Sequence (`longestConsecutive.py`)
Length of longest consecutive sequence in an unsorted array.
Example:
Input: [100,4,200,1,3,2]
Output: 4
Approach:
- Brute: sort then count. O(n log n).
- Optimal: hash set, start from sequence heads. O(n).

## Majority Element (> n/2) (`majorityElement1.py`)
Find the element appearing more than n/2 times.
Example:
Input: [2,2,1,1,2]
Output: 2
Approach:
- Brute: count frequencies. O(n) space.
- Optimal: Boyer-Moore voting. O(n), O(1) space.

## Maximum Subarray Sum (Kadane) (`maximumSubarraySum.py`)
Find maximum sum of a contiguous subarray.
Example:
Input: [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Approach:
- Brute: all subarrays. O(n^2).
- Optimal: Kadane's algorithm. O(n).

## Maximum Subarray Sum (Variation) (`maximumSubarraySumV2.py`)
Same problem with additional tracking (e.g., indices).
Example:
Input: [1,2,3,-2,5]
Output: 9
Approach:
- Brute: all subarrays. O(n^2).
- Optimal: Kadane with index tracking. O(n).

## Next Permutation (`nextPermutation.py`)
Transform to next lexicographic permutation.
Example:
Input: [1,2,3]
Output: [1,3,2]
Approach:
- Brute: generate all permutations and pick next. O(n!).
- Optimal: find pivot, swap, reverse suffix. O(n).

## Rearrange by Sign (`reArrange.py`)
Rearrange array to alternate positive and negative numbers.
Example:
Input: [1,2,-3,-1,-2,3]
Output: [1,-3,2,-1,3,-2]
Approach:
- Brute: separate positives/negatives, then merge. O(n) space.
- Optimal: in-place variant if counts are balanced. O(n).

## Two Sum (`twoSum.py`)
Find indices of two numbers that sum to target.
Example:
Input: [2,7,11,15], target=9
Output: [0,1]
Approach:
- Brute: check all pairs. O(n^2).
- Optimal: hash map of value to index. O(n).

## Set Matrix Zeroes (`matrixZeroes.py`)
If a cell is 0, set its row and column to 0.
Example:
Input:
[ [1,1,1],
  [1,0,1],
  [1,1,1] ]
Output:
[ [1,0,1],
  [0,0,0],
  [1,0,1] ]
Approach:
- Brute: mark rows/cols, then zero. O(n*m) space.
- Optimal: use first row/col as markers. O(1) extra space.

## Rotate Matrix 90 Deg (`RotateMatrix.py`)
Rotate an n x n matrix clockwise.
Example:
Input:
[ [1,2],
  [3,4] ]
Output:
[ [3,1],
  [4,2] ]
Approach:
- Brute: use extra matrix. O(n^2) space.
- Optimal: transpose + reverse rows. O(1) extra space.

## Spiral Matrix (`spiralMatrix.py`)
Return elements in spiral order.
Example:
Input:
[ [1,2,3],
  [4,5,6],
  [7,8,9] ]
Output: [1,2,3,6,9,8,7,4,5]
Approach:
- Brute: simulate with visited matrix. O(n*m) space.
- Optimal: boundary traversal. O(1) extra space.

## Subarrays With Given Sum (`subArraysWithSum.py`)
Count subarrays with sum equal to K.
Example:
Input: [1,2,3], K=3
Output: 2
Approach:
- Brute: all subarrays. O(n^2).
- Optimal: prefix sum + hashmap counts. O(n).
