# Group Anagrams

## Problem Statement
Given an array of `strs`, group the anagrams together. Order does not matter.

## Approach
1. **Idea**  
   Use a hash map with lists, appending to the list with each anagram. Define anagrams by an array of size 26, where the values are the number of times each letter occurs. I.e., index 0 is the number of times `a` occurs, index 1 `b`, etc.
2. **Steps/Pseudocode**  
   1. Initialize a hash map with a list as its default value. 
   2. Go through each string, and each character in the string, incrementing the value of the current character in the array.
   3. Append the string to the list whose key is the array from step 2.
   4. Return the values of the hash map.

## Complexity Analysis
- **Time Complexity**:  
  $O(nk)$: Where $n$ is the number of strings and $k$ is the maximum size of a string. 
- **Space Complexity**:  
  $O(nk)$: The hash map contains each string.
