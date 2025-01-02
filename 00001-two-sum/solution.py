from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Crucical observation:
        # We search num1 + num2 = target
        # Doing basic algebra, we get num1 = target - num2

        # Setup an empty hashmap (dictionary)
        hashmap = {}

        for i in range(len(nums)):
            # Find the complement
            comp = target - nums[i]

            # If the complement is a key in thehashmap, then we have found all the
            # numbers we need in order to get the indices.
            if comp in hashmap:
                return [i,hashmap[comp]]

            # Store the indices in thehashmap, where the number is the key, and
            # the index the value.
            hashmap[nums[i]] = i
        return []
