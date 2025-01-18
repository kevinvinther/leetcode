# Longest Consecutive Sequence

## Problem Statement
Given an unsorted array of integers, return the length of the longest sequence of consecutive integers in the array.

## Approach
1. **Idea**  
   Use a HashSet to check if the next available element exists. A HashSet is perfect for this, as it can find if the element exists in $O(1)$ average time.
2. **Steps/Pseudocode**  
    1. Initialize the numbers as a HashSet and initialize a variable that will contain the number of elements in the longest consecutive sequence. 
    2. For each number in the HashSet, check if it is the first number of a sequence (i.e., if $num-1$ exists).
    3. If *no*: Go to the next number.
    4. If *yes*: Make a new variable holding the current number, and set the sequence length to be 1. 
    5. (Assuming Yes) Use a while loop to check if $num+1$ exists, and increment $num$ as well as the variable holding the length. 
    6. (Assuming Yes) Set the value of the variable containing the length to be equal to the max of its old value, and the value of the length of the current sequence.

## Complexity Analysis
- **Time Complexity**:  
  $O(n)$: We go through over each element only once.
- **Space Complexity**:  
  $O(n)$: The HashSet contains each element at most once.

