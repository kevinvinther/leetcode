from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Initializes the hashmap with a list in each value
        hashmap = defaultdict(list)

        for s in strs:
            arr = [0] * 26
            for c in s:
                # 0 = a, 1 = b, etc. Makes "aaa" unique from "aa".
                arr[ord(c) - ord('a')] += 1
            hashmap[tuple(arr)].append(s)

        # The values are the lists
        return list(map.values())
