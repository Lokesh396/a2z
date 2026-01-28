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

def divide(dividend: int, divisor: int) -> int:
    if dividend == divisor:
        return 1
    
    sign = True
    if dividend < 0 and divisor > 0:
        sign = False
    if dividend >= 0 and divisor < 0:
        sign = False
    
    n = abs(dividend)
    d = abs(divisor)
    quotient = 0
    while n >= d:

        cnt = 0

        while n >= (d << (cnt+1)):
            cnt += 1
        quotient += (1 << cnt)
        n -= (d << cnt)
    
    if quotient == (1 << 31) and sign:
        return (1 << 31) -1

    if quotient == (1 << 31) and not sign:
        return -(1<<31)        

    return quotient if sign else -quotient 

def main():
    # -------------------------
    # WRITE YOUR LOGIC BELOW
    # -------------------------
    dividend = int(input())
    divisor = int(input())
    print('Divide with out / % *', divide(dividend=dividend, divisor=divisor))
    return 0

if __name__ == "__main__":
    # Note: These prints will go to output.txt if USE_FILE is True
    main()