# Merge Strings Alternately

## Problem Statement
You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.

Return the merged string.

## Approach
### Idea
The idea is very simple. We use two pointers, one for each word. While the pointers are less than the length of their respective words, we add the letter of the first pointers index of the first word to a new list (or mutable string, if you will), and then the second pointers element. We increment both. We must make sure not to go out of bounds, so we keep checking that we are inbounds.

### Steps/Pseudocode
```python
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
```

## Complexity Analysis
- **Time Complexity**:  
  $O(\max{n, k})$: Where $n$ is the size of `word1`, while $k$ is the size of `word2`.
- **Space Complexity**:  
  $O(n+k)$. The new string will be combined to have the size of `word1` plus `word2`.

## Notes / Edge Cases
Rather than using `while p1 < len(word1) ...`, you can do the following:

```python
n = max(len(word1), len(word))

for i in range(n):
  if i < len(word1):
    result += word1[i]
  if i < len(word2):
    result += word2[i]
```

This cleans the code up a bit, but the other version uses a two-pointer approach, which is a good technique to learn.

