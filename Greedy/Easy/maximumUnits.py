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

def maximumUnits(boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes = sorted(boxTypes, key=lambda x: -x[1])

        totalUnits = 0
        boxesPicked = 0
        for box, units in boxTypes:
            boxes = min(truckSize-boxesPicked, box)
            boxesPicked += boxes
            if boxes == 0:
                break
            totalUnits += (boxes * units)
        
        return totalUnits

def main():
    # -------------------------
    # WRITE YOUR LOGIC BELOW
    # -------------------------
    w = int(input())
    boxes = list(map(int, input().split()))
    units = list(map(int, input().split()))
    print('Maximum value:', maximumUnits(zip(boxes, units), w))
    return 0

if __name__ == "__main__":
    # Note: These prints will go to output.txt if USE_FILE is True
    main()