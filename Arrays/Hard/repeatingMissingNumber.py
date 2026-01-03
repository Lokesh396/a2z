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


def missingAndRepeating(arr, n):
   
   sqsum = 0
   nsum = 0 
   for num in arr:
       sqsum += (num**2)
       nsum += num
   
   fnsum = (n*(n+1)) // 2
   fnssqum = (n*(n+1)*(2*n+1)) // 6
   xmy = nsum - fnsum
   x2my2 = sqsum - fnssqum
   xpy = x2my2 // xmy
   tx = xmy+xpy
   x = tx // 2
   y = xpy - x

   return y, x

def missingAndRepatingXor(arr, n):

    xor = 0
    for i in range(n):
        xor = xor ^ arr[i]
        xor ^= i+1
    
    setbit = 0
    while 1:
        if xor & (1<<setbit):
            break
        else:
            setbit += 1
    
    ones = 0
    zeroes = 0
    for i in range(n):
        if arr[i] & (1<<setbit):
            ones ^= arr[i]
        else:
            zeroes ^= arr[i]
        
        if (i+1) & (1<<setbit):
            ones ^= i+1
        else:
            zeroes ^= i+1
    
    cnt = 0
    for num in arr:
        if num == zeroes:
            cnt += 1
    
    return (ones, zeroes) if cnt == 2 else (zeroes, ones)

def main():
    # -------------------------
    # WRITE YOUR LOGIC BELOW
    # -------------------------
    arr = list(map(int, input().split()))
    print('missing and repeating numbers are:', missingAndRepeating(arr, 5))
    print('missing and repeating numbers are:', missingAndRepatingXor(arr, 5))
    return 0

if __name__ == "__main__":
    # Note: These prints will go to output.txt if USE_FILE is True
    main()