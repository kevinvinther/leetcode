from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Make a hashset containing the numbers
        s = set(nums)
        # Longest consecutive found
        longest = 0

        # Go through each number in the hash set
        for num in s:
            # If we are at a smallest number in a (possible) sequence
            if num - 1 not in s:
                curNum = num
                current = 1

                # While the next number exists in sequence, iterate to the next
                # and increment the length of the sequence (current) with 1.
                while curNum + 1 in s:
                    current += 1
                    curNum += 1

                # Let longest be the longest of the current sequence, and any
                # older sequences.
                longest = max(longest, current)

        return longest
