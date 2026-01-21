# Binary Search - 2D Arrays

Concise revision notes for the problems in this folder.

## Search in 2D Matrix (`search2DMatrix.py`)
Search target in a row-wise sorted matrix where rows are contiguous.
Example:
Input:
[ [1,3,5],
  [7,9,11],
  [13,15,17] ], target=9
Output: True
Approach:
- Brute: scan all cells. O(n*m).
- Optimal: treat as 1D and binary search. O(log(n*m)).

## Search in 2D Matrix II (`search2DMatrixII.py`)
Search target in matrix with rows and columns sorted.
Example:
Input:
[ [1,4,7],
  [2,5,8],
  [3,6,9] ], target=5
Output: True
Approach:
- Brute: scan all cells. O(n*m).
- Optimal: start from top-right and eliminate row/col. O(n+m).

## Row with Max 1s (`rowMaxOnes.py`)
Find the row index with maximum number of 1s in a binary matrix.
Example:
Input:
[ [0,0,1,1],
  [0,1,1,1],
  [0,0,0,1] ]
Output: 1
Approach:
- Brute: count 1s per row. O(n*m).
- Optimal: binary search first 1 in each row or sweep from top-right. O(n log m) or O(n+m).

## Matrix Median (`matrixMedian.py`)
Find median of a row-wise sorted matrix.
Example:
Input:
[ [1,3,5],
  [2,6,9],
  [3,6,9] ]
Output: 5
Approach:
- Brute: flatten and sort. O((n*m) log(n*m)).
- Optimal: binary search on value range with upper bounds. O(n log m * log range).

## Peak Element II (`peakElementII.py`)
Find a peak element in 2D grid.
Example:
Input:
[ [10,8,10,10],
  [14,13,12,11],
  [15,9,11,21],
  [16,17,19,20] ]
Output: peak value 21 (index may vary)
Approach:
- Brute: check all cells vs neighbors. O(n*m).
- Optimal: binary search on columns and take max in mid column. O(n log m).
