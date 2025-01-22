class Solution:
    def reverseVowels(self, s: str) -> str:
        s = list(s)

        p1 = 0
        p2 = len(s)-1

        vowels = "aeiouAEIOU"

        while p1 < p2:
            while s[p1] not in vowels and p1 < p2:
                p1 += 1
            while s[p2] not in vowels and p1 < p2:
                p2 -= 1

            s[p1], s[p2] = s[p2], s[p1]
            p1 += 1
            p2 -= 1

        return s
