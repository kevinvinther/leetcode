# Valid Parentheses

## Problem Statement
Given a string `s` containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

## Approach
1. **Idea**  
   Let a dictionary contain the end symbols and their counterpart, i.e. ')': '('. If the symbol we encounter is in the dictionary, we check if the top layer of the stack is the value of the key and the stack is not empty, and if so, we pop, if not, we return that it is not valid (i.e. `false`).
2. **Steps/Pseudocode**  
   1. Initialize a dictionary containing the pairings
   2. Initialize the stack 
   3. Go through each character, and if it is in the dictionary, check if it can be popped. If it can, pop it, if not return false. If it is not a part of the dictionary. append it to the stack. 
   4. If the stack is empty, return true, otherwise return false.

## Complexity Analysis
- **Time Complexity**:  
  $O(n)$: We do constant work at each character of $n$ characters.
- **Space Complexity**:  
  $O(n)$: The stack holds at most all of the characters.

