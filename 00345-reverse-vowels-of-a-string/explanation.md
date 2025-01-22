# Reverse Vowels of a String

## Problem Statement
Given a string s, reverse only all the vowels in the string and return it.

## Approach
1. **Idea**  
   1. Convert the string to a list, or another mutable, iterable type. 
   2. Have two pointers, one beginning at start of the list, the other at the end.
   3. Respectively increment/decrement the pointer, until they're both at vowels, and swap. 
   4. Continue until the first pointer and the second pointer's values are equal.

## Complexity Analysis
- **Time Complexity**:  
  $O(n)$: There is done constant work on each element in the list. 
- **Space Complexity**:  
  $O(n)$: The list `s` is held in memory, along with each pointer. `s` is of size $n$, while the pointers are of constant size.
