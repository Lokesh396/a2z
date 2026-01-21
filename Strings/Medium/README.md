# Strings - Medium

Concise revision notes for the problems in this folder with slightly richer descriptions.

## String to Integer (ATOI) (`atoi.py`)
Convert a string to an integer following sign and overflow rules.
Example:
Input: "   -42"
Output: -42
Approach:
- Brute: parse manually with validation. O(n).
- Optimal: same, using bounds checks for overflow. O(n).

## Beauty Sum (`beautySum.py`)
For all substrings, sum (max frequency - min frequency) of characters.
Example:
Input: "aabcb"
Output: 5
Approach:
- Brute: generate all substrings and count freq. O(n^3).
- Optimal: expand from each start with freq counts. O(n^2).

## Count Substrings With K Distinct (`countSubstringsWithk.py`)
Count substrings that contain exactly k distinct characters.
Example:
Input: s="pqpqs", k=2
Output: 7
Approach:
- Brute: check all substrings with set. O(n^2).
- Optimal: atMost(k) - atMost(k-1) using sliding window. O(n).

## Maximum Nesting Depth of Parentheses (`maximumNestDepth.py`)
Find maximum depth of nested parentheses in a string.
Example:
Input: "(1+(2*3)+((8)/4))+1"
Output: 3
Approach:
- Brute: use stack, track max size. O(n).
- Optimal: counter increment/decrement. O(n), O(1) space.

## Sort Characters by Frequency (`sortByFrequency.py`)
Return string characters sorted by decreasing frequency.
Example:
Input: "tree"
Output: "eetr" (or "eert")
Approach:
- Brute: count and sort by frequency. O(n log n).
- Optimal: bucket sort by frequency. O(n).

## Reverse Words in String (`reverseWords.py`)
Reverse the order of words, trimming extra spaces.
Example:
Input: "  hello world  "
Output: "world hello"
Approach:
- Brute: split and reverse list of words. O(n).
- Optimal: manual parse to avoid extra space use. O(n).

## Roman to Integer (`romanToInteger.py`)
Convert a Roman numeral to integer using subtraction rules.
Example:
Input: "MCMXCIV"
Output: 1994
Approach:
- Brute: map symbols and scan with lookahead. O(n).
- Optimal: same with simple condition checks. O(n).
