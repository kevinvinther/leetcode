class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        new_string = []

        p1 = 0
        p2 = 0

        while p1 < len(word1) or p2 < len(word2):
            if p1 < len(word1):
                new_string.append(word1[p1])
                p1 += 1
            if p2 < len(word2):
                new_string.append(word2[p2])
                p2 += 1


        return "".join(new_string)
