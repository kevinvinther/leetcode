class Solution:
    def isValid(self, s: str) -> bool:
        matchings = {
            ")": "(",
            "]": "[",
            "}": "{"
        }

        stack = []

        for c in s:
            if c in matchings:
                if not stack or matchings[c] != stack[-1]:
                    return False
                else:
                    stack.pop()
            else:
                stack.append()
        return not stack
