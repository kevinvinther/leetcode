from collections import defaultdict
from typing import List

class Solution:
    def compress(self, chars: List[str]) -> int:
        index = 0
        res = 0

        while index < len(chars):
            group_size = 0

            while index + group_size < len(chars) and chars[index] == chars[index + group_size]:
                group_size += 1

            chars[res] = chars[index]
            res += 1

            if group_size > 1:
                s = str(group_size)
                l = len(s)
                chars[res:res+l] = s
                res += l

            index += group_size

        return res
