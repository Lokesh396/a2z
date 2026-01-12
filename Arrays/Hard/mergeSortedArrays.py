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



def optimalv1(arr1, arr2):
    """
    Given two sorted arrays merge them with out using any extra space.

    Algorithm:
    - from the array1 we start from last and from the array2 we start from first and swap until 
    elements in the left array is greater than the array2.
    - finally we sort them and return.

    Args:
        arr1: sorted array 1
        arr2: sorted array 2

    Returns: modifies the arrays in place such that elements in the left array is smaller than or
    equal to the elements in the right.

    Time Complexity: O(min(m,n)) + o(mlgm) + o(nlgn)

    Space Complexity: O(1)
    """
    left = len(arr1) - 1
    right = 0
    while left >= 0 and right < len(arr2):

        if arr1[left] > arr2[right]:
            arr1[left], arr2[right] = arr2[right], arr1[left]
            left -= 1
            right += 1
        else:
            break
    arr1.sort()
    arr2.sort()


def swap(arr1, arr2, left, right):
    if arr1[left] > arr2[right]:
        arr1[left], arr2[right] = arr2[right], arr1[left]

def optimalv2(arr1, arr2):

    """
    we use the gap method to sort the arrays.

    Algorithm:
    - we will take a gap of length /2 at first and compare the elements and swap.
    - we will have three scenarios here:
        - both elements in left array
        - both elements in right array
        - one is left and one in right
    - gap becomes gap / 2 + (gap & 1)
    - we repeat these until becomes gap becomes 1.
    Args:
        arr1: input sorted array1
        arr2: input sorted array2

    Returns: modifies the arrays inplace

    Time Complexity: O(m+n)lg(m+n)

    Space Complexity: O(1)
    """

    m = len(arr1)
    n = len(arr2)
    length = m + n
    gap = length // 2  + (length & 1)

    while gap > 0:

        left = 0
        right = left + gap

        while right < length:
            if left < m and right >= m:
                swap(arr1, arr2, left, right-m)
               
            elif left >= m:
                swap(arr2, arr2, left-m, right-m)
            else:
                swap(arr1, arr1, left, right)

            left += 1
            right += 1
            print(left, right, length)
        if(gap != 1):
            gap = gap // 2 + (gap & 1)
        else:
            gap = 0
        
def leetcode_version(arr1, arr2, m, n):

    i =  m - 1
    j =  n - 1
    k = (m+n) - 1

    while j >= 0:
        if i >= 0 and arr1[i] > arr2[j]:
            arr1[k] = arr1[i]
            i -= 1
        else:
            arr1[k] = arr2[j] 
            j -= 1
        
        k -= 1



def main():
    # -------------------------
    # WRITE YOUR LOGIC BELOW
    # -------------------------
    
    arr1 = list(map(int, input().split()))
    arr2 = list(map(int, input().split()))
    # optimalv1(arr1, arr2)
    # optimalv2(arr1, arr2)
    leetcode_version(arr1, arr2, 4, 4)
    print("Arrays after merging:", arr1, arr2)
    return 0

if __name__ == "__main__":
    # Note: These prints will go to output.txt if USE_FILE is True
    main()