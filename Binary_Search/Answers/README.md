# Binary Search - Answers

Concise revision notes for the problems in this folder.

## Square Root (Integer) (`squareRoot.py`)
Find floor of sqrt(n).
Example:
Input: n=10
Output: 3
Approach:
- Brute: check i*i <= n. O(sqrt n).
- Optimal: binary search on range. O(log n).

## Nth Root of M (`nRootM.py`)
Find integer x such that x^n = m (or report none).
Example:
Input: n=3, m=27
Output: 3
Approach:
- Brute: test all x. O(m^(1/n)).
- Optimal: binary search on x. O(log m).

## Koko Eating Bananas (`kokoEatingBananas.py`)
Minimum eating speed to finish piles in h hours.
Example:
Input: piles=[3,6,7,11], h=8
Output: 4
Approach:
- Brute: try all speeds. O(maxPile * n).
- Optimal: binary search on speed. O(n log maxPile).

## Make Bouquets (`makeMboquets.py`)
Minimum day to make m bouquets of size k.
Example:
Input: bloom=[1,10,3,10,2], m=3, k=1
Output: 3
Approach:
- Brute: try all days. O(range * n).
- Optimal: binary search on day. O(n log range).

## Smallest Divisor With Threshold (`smallestDivisorThreshold.py`)
Smallest divisor so sum(ceil(ai/div)) <= threshold.
Example:
Input: nums=[1,2,5,9], threshold=6
Output: 5
Approach:
- Brute: try all divisors. O(maxVal * n).
- Optimal: binary search on divisor. O(n log maxVal).

## Capacity to Ship Packages (`capacityToShipPackges.py`)
Min ship capacity to ship within D days.
Example:
Input: weights=[1,2,3,4,5,6,7,8,9,10], D=5
Output: 15
Approach:
- Brute: try all capacities. O(range * n).
- Optimal: binary search on capacity. O(n log range).

## Gas Stations (Minimize Max Distance) (`gasStations.py`)
Minimize maximum distance between adjacent stations by adding k stations.
Example:
Input: stations=[1,2,3,4,5], k=2
Output: 1.0
Approach:
- Brute: greedy split repeatedly. O(k log n).
- Optimal: binary search on distance. O(n log range).

## Painter's Partition (`paintersPartition.py`)
Min time to paint boards with k painters (contiguous).
Example:
Input: boards=[10,20,30,40], k=2
Output: 60
Approach:
- Brute: try all max times. O(range * n).
- Optimal: binary search on max time. O(n log range).

## Split Array Largest Sum (`splitArray.py`)
Split array into k parts to minimize largest sum.
Example:
Input: [7,2,5,10,8], k=2
Output: 18
Approach:
- Brute: try all max sums. O(range * n).
- Optimal: binary search on max sum. O(n log range).

## Kth Missing Positive (`kthmissing.py`)
Find kth missing positive number.
Example:
Input: [2,3,4,7,11], k=5
Output: 9
Approach:
- Brute: simulate missing count. O(n+k).
- Optimal: binary search on index. O(log n).

## Kth Element of Two Sorted Arrays (`kthElementSortedArray.py`)
Find kth element in two sorted arrays.
Example:
Input: a=[2,3,6,7,9], b=[1,4,8,10], k=5
Output: 6
Approach:
- Brute: merge arrays. O(n+m).
- Optimal: binary search on partition. O(log min(n,m)).

## Median of Two Sorted Arrays (`medianSortedArrays.py`)
Find median of two sorted arrays.
Example:
Input: a=[1,3], b=[2]
Output: 2.0
Approach:
- Brute: merge then median. O(n+m).
- Optimal: binary search on partition. O(log min(n,m)).

## Aggressive Cows (`agressiveCows.py`)
Place k cows to maximize minimum distance.
Example:
Input: stalls=[1,2,4,8,9], k=3
Output: 3
Approach:
- Brute: try all distances. O(range * n).
- Optimal: binary search on distance. O(n log range).

## Allocate Books (`allocateBooks.py`)
Allocate books to minimize maximum pages per student.
Example:
Input: pages=[12,34,67,90], students=2
Output: 113
Approach:
- Brute: try all max pages. O(range * n).
- Optimal: binary search on max pages. O(n log range).
