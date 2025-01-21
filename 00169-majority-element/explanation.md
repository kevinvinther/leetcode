# Majority Element

## Problem Statement
Given an array of numbers, return the element occurring more than $\lfloor n / 2 \rfloor$ times.

## Approach
1. **Idea**  
   Use the Boyer-Moore Voting Algorithm. 
   1. The algorithm works by maintaining a "candidate" for the majority element and a count of how many times this candidate has been "supported" by the elements seen so far.
2. **Steps/Pseudocode**  
   1. Initialize two variables: `candidate` and `occurences`.
    * Candidate keeps track of what it will return if the array is to end now.
    * Occurences keeps track of the support for the candidate.
   2. Iterate through the array:
    * If `occurences` is 0, update `candidate` to the current element, and set `occurences` to 1.
    * Otherwise: 
        * If the current element is equal to `majority`, increment `occurences`.
        * If not, decrement `occurences`.

## Complexity Analysis
- **Time Complexity**:  
  $O(n)$: The algorithm does $O(1)$ work for each element in the array.
- **Space Complexity**:  
  $O(1)$: Constant space.

