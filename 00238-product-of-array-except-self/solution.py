from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> None:
        # Create arrays filled with 0's for the left product, the right
        # product, and the result
        left = [0] * len(nums)
        right = [0] * len(nums)
        res = [0] * len(nums)

        # Let the first index of left be 1 such that we can multiply
        # properly.
        left[0] = 1
        for i in range(1, len(nums)):
            # The index is equal to the cumulative product
            left[i] = left[i-1] * nums[i-1]

        # Repeat for the right side
        right[len(nums)-1] = 1
        for i in range(len(nums)-2, -1, -1):
            right[i] = right[i+1] * nums[i+1]
            # While calculating the right side, do the result as well.
            # This is simply found by multiplying the cumulative left
            # and right sides, up untill the current index.
            res[i] = right[i] * left[i]

        # As the loop didn't get the last one, we put this in manually.
        res[len(nums)-1] = right[len(nums)-1] * left[len(nums)-1]

        return res
