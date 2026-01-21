# Strings - Easy

Concise revision notes for the problems in this folder with slightly richer descriptions.

## Valid Anagram (`anagram.py`)
Check whether two strings are anagrams (same characters with same counts, order doesn't matter).
Example:
Input: s="anagram", t="nagaram"
Output: True
Approach:
- Brute: sort both strings and compare. O(n log n).
- Optimal: frequency count for 26 letters (or hashmap). O(n).

## Isomorphic Strings (`isomorphicString.py`)
Determine if characters in one string can be mapped one-to-one to form the other string.
Example:
Input: s="egg", t="add"
Output: True
Approach:
- Brute: try building mapping and validate both directions. O(n).
- Optimal: maintain two maps to ensure bijection. O(n).

## String Rotation (`stringRotation.py`)
Check if one string is a rotation of another (cyclic shift).
Example:
Input: s="abcde", goal="cdeab"
Output: True
Approach:
- Brute: generate all rotations. O(n^2).
- Optimal: check if goal is substring of s+s. O(n).

## Largest Odd Number in String (`largestOddNumber.py`)
Given a numeric string, return the largest odd-number substring (prefix).
Example:
Input: "35427"
Output: "35427"
Approach:
- Brute: check all prefixes from longest to shortest. O(n^2).
- Optimal: scan from right to find first odd digit. O(n).

## Longest Common Prefix (`longestCommonPrefix.py`)
Find the longest common starting substring among all strings.
Example:
Input: ["flower","flow","flight"]
Output: "fl"
Approach:
- Brute: compare character by character across all strings. O(n*m).
- Optimal: sort array and compare first/last. O(n log n).
