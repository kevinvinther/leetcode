from collections import Counter

class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if len(s) < k:  # Cannot be split into more than there are characters
            return False

        count = Counter(s)  # Makes a frequency dictionary
        odd = 0

        for c in count.values():
            odd += c % 2  # c % 2 == 1 if c is odd

        return odd <= k
