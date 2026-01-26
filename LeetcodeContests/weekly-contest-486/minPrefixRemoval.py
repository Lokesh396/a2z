from typing import List

class Solution:
    def minimumPrefixLength(self, nums: List[int]) -> int:
        right = len(nums)-1
        while right >= 0:
            if right == 0:
                return 0
            if nums[right-1] <= nums[right] -1:
                right -= 1
            else:
                break
        return right