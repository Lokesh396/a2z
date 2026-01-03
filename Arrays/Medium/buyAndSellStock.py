import sys
import os
from pathlib import Path
from typing import List

# Fast I/O and Recursion Setup
sys.setrecursionlimit(2000)
input = sys.stdin.readline

USE_FILE = True

if USE_FILE:
    BASE_DIR = Path(__file__).resolve().parents[2]
    sys.stdin = open(os.path.join(BASE_DIR, "input.txt"), "r")
    sys.stdout = open(os.path.join(BASE_DIR, "output.txt"), "w")

def maxProfit(prices:List[int]):
    """
    
    Given an array of stock prices, we need to return the maximum profit we can get.

    Algorithm:
    - we iterate through the array, and check for the maximum profit, by tracking the left min for the
    current element.

    Args:
        prices: input array that contains stock prices.

    Returns: Returns the maximum profit

    Time Complexity: O(n) just a linear traversal of the array.
    
    Space Complexity: O(1) no extra space is required.

    """
    mini = prices[0]
    profit = 0
    for i in range(1, len(prices)):
        cost = prices[i] - mini
        profit = max(profit, cost)
        mini = min(mini, prices[i])


    return profit
def main():
    # -------------------------
    # WRITE YOUR LOGIC BELOW
    # -------------------------
    arr = list(map(int, input().split()))
    print('max Profit: ', maxProfit(arr))
    return 0

if __name__ == "__main__":
    # Note: These prints will go to output.txt if USE_FILE is True
    main()