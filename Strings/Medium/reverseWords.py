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

def reverseWords( s: str) -> str:

    """
    Given a string we need to rotate the string by words.

    Algorithm:
    - we start from the back and ignore the leading whitespaces and we store the first encountered
    charachter.
    - we will move the left until the window is valid, if we encounter a whitespace, thats the start
    of the word, we store that word in the result.

    Args:
        - s: input string
    
    Returns: returns the string after reversing.

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
        
def main():
    # -------------------------
    # WRITE YOUR LOGIC BELOW
    # -------------------------
    s = input()
    print('reverse words:', reverseWords(s))
    return 0

if __name__ == "__main__":
    # Note: These prints will go to output.txt if USE_FILE is True
    main()