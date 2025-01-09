from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""

        # Choose an arbitrary string, in this algorithm we choose strs[0]
        for i in range(len(strs[0])):
            for s in strs:
                # Make sure it is within bounds, otherwise we'll get errors.
                # If it is within bounds, but we have come to a place, where
                # the string we've chosen does not contain the same letter
                # at the current index, then we return up until that point.
                if i == len(s) or s[i] != strs[0][i]:
                    return res
            res += strs[0][i]

        # At this point we've chosen the shortest string and it is also equal
        # to the longest prefix.
        return res
