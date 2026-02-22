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

def maximumValue(items, n, w):

	# Write your code here.
	# ITEMS contains [weight, value] pairs.

	items = sorted(items, key = lambda x : -(x[1] / x[0]))
	alreadyPicked = 0
	total = 0
	for weight, value in items:
		minWeight = min(w-alreadyPicked, weight)
		if minWeight == 0:
			break
		alreadyPicked += minWeight
		total += (minWeight * (value/weight))
	
	return total

def main():
    # -------------------------
    # WRITE YOUR LOGIC BELOW
    # -------------------------
    w = int(input())
    weights = list(map(int, input().split()))
    values = list(map(int, input().split()))
    print('Maximum value:', maximumValue(zip(weights, values),len(weights), w))
    return 0

if __name__ == "__main__":
    # Note: These prints will go to output.txt if USE_FILE is True
    main()