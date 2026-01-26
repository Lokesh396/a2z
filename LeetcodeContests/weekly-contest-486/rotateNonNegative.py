from typing import List

class Solution:
    def rotate(self,arr, k):
        arr[:k]= arr[:k][::-1]
        arr[k:] = arr[k:][::-1]
        return arr[::-1]
    def rotateElements(self, nums: List[int], k: int) -> List[int]:
        pos = []
        for num in nums:
            if num >= 0:
                pos.append(num)
        if not len(pos):
            return nums
        k = k % len(pos)
        if not k:
            return nums
        arr = self.rotate(pos, k)
        idx = 0
        for i in range(len(nums)):
            if nums[i] >= 0:
                nums[i] = arr[idx]
                idx += 1

        return nums