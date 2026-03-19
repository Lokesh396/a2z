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

def myPow(x: float, n: int) -> float:
    if n == 0:
        return 1
    
    if n == 1:
        return x
    
    def power(n):
        """
        Given a number x and the power n , we need to return the value of x when we rise
        it to power n.

        Algorithm:
        - the base case is when n reaches 1 then we can return x as x^1 is x.
        -we divide the n by 2 at every step and accumulate the result, if the n is odd we will
        multiply x to the ans.
        - we finally reutrn our ans if n is even else we return 1/ans

        Args:
            n : power
        
        Time Complexity: O(lgn)

        Space Complexity: O(1)
        
        """
        if n < 0:
            n = n * -1
        if n == 1:
            return x
        
        temp = power(n//2)
        ans = temp * temp
        if n & 1:
            ans *= x
        
        return ans
    
    ans = power(n)
    if n < 0:
        return 1 / ans
    return ans
def main():
    # -------------------------
    # WRITE YOUR LOGIC BELOW
    # -------------------------
    
    return 0

if __name__ == "__main__":
    # Note: These prints will go to output.txt if USE_FILE is True
    main()