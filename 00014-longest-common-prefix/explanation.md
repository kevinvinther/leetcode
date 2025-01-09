# [Problem Title]

## Problem Statement
Given a list of strings, find the longest prefix common to all strings.

## Approach
1. Choose an arbitrary string of the strings. 
2. Loop over all strings, and check if their index is equal to the arbitrary strings index. 
3. If not, return what we have until now. 
4. If yes, add this letter to our result. 
5. If we get to the end of the arbitrary string, this was the shortest, and also equal to the longest common prefix. We return the result.

## Complexity Analysis
- **Time Complexity**:  
  $O(n \cdot m)$. If $n$ is the size of the array and $m = \min(length of string)$. We go over the list until we cannot anymore. We cannot go over the list anymore, when we have crossed the boundaries of the minimum length string.
- **Space Complexity**:  
  $O(m)$. The return array can have up to $m$ letters. 
