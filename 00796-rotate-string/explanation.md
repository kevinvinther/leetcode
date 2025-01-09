# Rotate String

## Problem Statement
Given two strings, $s$ and $goal$, return *true* if and only if $s$ can become $goal$ after some number of *shifts* on $s$.

## Approach
1. **Idea**  
   Make the observation that if the $goal$ string is to be found in $s+s$ (where + is appending), then it can be shifted. 
2. Check first if the length of the two strings are the same
 - If not: $goal$ cannot be shifted into $s$, no matter what. 
 - If true: Check if $goal$ can be found in $s+s$. Using python this syntax is simple: `goal in s+s`. However, this can also be done in a simple loop.

## Complexity Analysis
- **Time Complexity**:  
  $O(n)$. Concatenation and search each take $O(n)$ time. (See KMP or Rabin-Karp for search algorithms.)
- **Space Complexity**:  
  $O(1)$. No additional data structures are created.
