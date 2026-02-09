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
def reverseWords(s: str) -> str:

    """
    Given a string which may contain trailing spaces, rotate the words in the string.

    Algorithm:
    - we will iterate from the right and decrement as long as we find non empty characther, that is end
    of the word, then we will try to find the empty space, to mark the start of the word, we will add
    that too our result string and we will return it finally.

    Args:
        s: input string
    
    Returns: returns the resultant string

    Time Complexity: O(n)

    Space Complexity: O(n)
    """
    res = ''

    right = len(s) -1

    while right >= 0:

        while right >= 0 and s[right] == " ":
            right -= 1
        
        if right < 0: break
        j = right

        while right >= 0 and s[right] != " ":
            right -= 1
        
        if res:
            res += " "

        res += s[right+1:j+1]
    
    return res
        
def main():
    # -------------------------
    # WRITE YOUR LOGIC BELOW
    # -------------------------
    s = input()
    print('Reverse Words:', reverseWords(s))
    return 0

if __name__ == "__main__":
    # Note: These prints will go to output.txt if USE_FILE is True
    main()