import sys
import os
from pathlib import Path
from collections import defaultdict

# Fast I/O and Recursion Setup
sys.setrecursionlimit(2000)
input = sys.stdin.readline

USE_FILE = True

if USE_FILE:
    BASE_DIR = Path(__file__).resolve().parents[2]
    sys.stdin = open(os.path.join(BASE_DIR, "input.txt"), "r")
    sys.stdout = open(os.path.join(BASE_DIR, "output.txt"), "w")

def atmostk(s, k):
    """
    Given a string we need to return the count of substring with at most k distinct characthers:

    Algorithm:
    - we will start iterating from the left and increment the char frequency by 1, at any point of time
    if the chars in the frequency map exceeds the k we will shrink the substring from left.
    - we will add all the valid substrings.
    - finally we will return the substrings count.

    Args: 
        - s: input string
        - k : distinct characther count
    
    Returns: returns the count of the valid substrings.

    Time Complexity: O(n)

    Space Complexity: O(k)
    """
    left =  0
    right = 0
    cnt = 0
    freqMap = defaultdict(int)
    while right < len(s):
        

        freqMap[s[right]] += 1
        while len(freqMap) > k:
            freqMap[s[left]] -= 1
            if freqMap[s[left]] == 0:
                del freqMap[s[left]]
            left += 1

        cnt += right - left + 1
        right += 1
    return cnt
def countSubStrings(s: str, k: int) -> int:
    # Write your code here
    # we call the function with k and k-1, as k contains all substrings with at most k distinct chars
    # k- 1 contains substrings with atmost k-1 different chars, their substracts gives us exactly k.
    return atmostk(s, k) - atmostk(s, k-1)

def main():
    # -------------------------
    # WRITE YOUR LOGIC BELOW
    # -------------------------
    s = input()
    print('substrings:', countSubStrings(s, 2))
    return 0

if __name__ == "__main__":
    # Note: These prints will go to output.txt if USE_FILE is True
    main()