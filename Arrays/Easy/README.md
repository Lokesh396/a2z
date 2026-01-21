# Arrays - Easy

Concise revision notes for the problems in this folder.

## Intersection of Two Arrays (`Intersection.py`)
Find the common elements between two arrays (typically sorted).
Example:
Input: arr1 = [1,2,2,3], arr2 = [2,2,4]
Output: [2,2]
Approach:
- Brute: check each element of arr1 in arr2; mark used. O(n*m).
- Optimal: two pointers on sorted arrays. O(n+m).

## Check If Array Is Sorted (`isSorted.py`)
Determine whether the array is non-decreasing.
Example:
Input: [1,2,2,4]
Output: True
Approach:
- Brute: compare every pair i<j. O(n^2).
- Optimal: single pass, fail if a[i] > a[i+1]. O(n).

## Largest Element (`largestElement.py`)
Return the maximum element in the array.
Example:
Input: [3,1,9,2]
Output: 9
Approach:
- Brute: sort and take last. O(n log n).
- Optimal: track max in one pass. O(n).

## Linear Search (`linearSearch.py`)
Find the index of a target element (or report not found).
Example:
Input: arr=[4,7,1], target=7
Output: 1
Approach:
- Brute: scan all elements. O(n).
- Optimal: same (no faster worst-case for unsorted arrays).

## Longest Subarray With Sum K (Positive Only) (`longestSubarrayWithSumkPos.py`)
Find the longest subarray with sum exactly K when all numbers are positive.
Example:
Input: arr=[1,2,1,1,1], K=3
Output: 2
Approach:
- Brute: all subarrays, track longest. O(n^2).
- Optimal: sliding window (two pointers). O(n).

## Longest Subarray With Sum K (With Negatives) (`longestSubarraywithSumK.py`)
Find the longest subarray with sum exactly K when negatives may exist.
Example:
Input: arr=[1,-1,5,-2,3], K=3
Output: 4
Approach:
- Brute: all subarrays. O(n^2).
- Optimal: prefix sum with hashmap of earliest index. O(n).

## Max Consecutive Ones (`maxConsecutiveOnes.py`)
Find the maximum length of consecutive 1s in a binary array.
Example:
Input: [1,1,0,1,1,1]
Output: 3
Approach:
- Brute: check all subarrays. O(n^2).
- Optimal: single pass, count streak. O(n).

## Move Zeroes (`moveZeroes.py`)
Move all zeroes to the end while maintaining order of non-zero elements.
Example:
Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
Approach:
- Brute: create new array, then fill zeros. O(n) extra space.
- Optimal: two-pointer in-place swap/overwrite. O(n).

## Remove Duplicates From Sorted Array (`removeDuplicates.py`)
Remove duplicates in-place and return new length.
Example:
Input: [1,1,2,2,3]
Output: length=3, array starts [1,2,3]
Approach:
- Brute: use set or extra array. O(n) space.
- Optimal: two-pointer overwrite. O(n).

## Rotate Array (`rotateArray.py`)
Rotate the array by k steps.
Example:
Input: [1,2,3,4,5], k=2
Output: [4,5,1,2,3]
Approach:
- Brute: rotate one step k times. O(n*k).
- Optimal: reverse parts or use extra array. O(n).

## Second Largest Element (`secondLargest.py`)
Return the second largest distinct element.
Example:
Input: [5,1,5,3]
Output: 3
Approach:
- Brute: sort and scan from end. O(n log n).
- Optimal: track largest and second largest in one pass. O(n).

## Single Number (`singleNumber.py`)
Find the element that appears once when others appear twice.
Example:
Input: [2,2,1]
Output: 1
Approach:
- Brute: frequency map. O(n) space.
- Optimal: XOR all elements. O(n), O(1) space.

## Union of Two Sorted Arrays (`unionofTwoSortedArrays.py`)
Return the union of two sorted arrays without duplicates.
Example:
Input: [1,2,2,3], [2,3,4]
Output: [1,2,3,4]
Approach:
- Brute: merge then remove duplicates. O((n+m) log (n+m)).
- Optimal: two pointers with skip duplicates. O(n+m).
