from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1

        while low <= high:
            med = (low + high) // 2
            if target == nums[med]:
                return med
            elif target < nums[med]:
                high = med - 1
            else:
                low = med + 1

        return -1
