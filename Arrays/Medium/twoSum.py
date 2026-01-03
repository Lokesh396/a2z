import sys
import os
from pathlib import Path

# Fast I/O and Recursion Setup
sys.setrecursionlimit(2000)
input = sys.stdin.readline

USE_FILE = True

if USE_FILE:
    BASE_DIR = Path(__file__).resolve().parents[2]
    sys.stdin = open(os.path.join(BASE_DIR, "input.txt"), "r")
    sys.stdout = open(os.path.join(BASE_DIR, "output.txt"), "w")
def twoSum( nums, target ):
    """
    
    Given an array of elements retun two indexes such that i != j, where arr[i] + arr[j] = target

    Algorithm:
    - We will use dictionary to store the indexes of every element in the array, and check whether
    target - num exists in the dictionary, if exists then there is a pair with i, j which sums
    upto target.

    Returns:Returns a list with two indexes.
    
    Time Complexity: O(n) one traversal of the array, and lookup in dictionary takes constant time.

    Space Complexity: O(n) all elements will be stored in the dictionary.

    Approach 2:
    - We can sort the array and use two pointers from left and right and get to know whether there
    exists two indexes which satisfies our requirement.

    Time Complexity: O(nlgn) any standard Sorting algorithm takes nlgn time.

    Space Complexity: O(n) Internally while merging recursive stack or in the merge procedure..
    """
    memory = dict()

    for idx, num in enumerate(nums):
        rem = target - num
        if rem in memory:
            return [memory[rem], idx]
        
        memory[num] = idx
def main():
    # -------------------------
    # WRITE YOUR LOGIC BELOW
    # -------------------------
    arr = list(map(int, input().split()))
    target = int(input())
    print('Target present at:', twoSum(arr, target=target))
    return 0

if __name__ == "__main__":
    # Note: These prints will go to output.txt if USE_FILE is True
    main()