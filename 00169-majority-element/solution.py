from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        occurences = 0
        candidate = None

        for num in nums:
            if occurences == 0:
                candidate = num
            if num == candidate:
                occurences += 1
            else:
                occurences -= 1

        return candidate
