# Binary Search

This is without a doubt one of the most important algorithms in Computer Science, along with being one of the simplest.

## Problem Statement
Given an array of integers which has been sorted along with another integer, which functions as the target, write a function to search for target in the array of integers. If the target exists, return the index, if not, return -1.

## Approach
1. **Idea**  
   Use binary search. 
2. **Steps/Pseudocode**  
   1. Make a high and low variable, containing the length of the array - 1, and the number 0, i.e., the beginning of the array.
   2. Start a while loop, which runs for as long as `low <= high`.
   3. Initialize a variable `med` to be the median of the array, i.e. $\lfloor \frac{(\text{low} + \text{high})}{2} \rfloor$.
   4. If the number at the index of `med` is equal to the target, return `med`.
   5. Otherwise, if $target \le nums[med]$, we know that the ceiling is $med-1$. Thus, we set `high` to be `med-1`. 
   6. Otherwise, target is greater than `nums[med]`, and thus we set `low` to be `med + 1`.
   7. If we are out of the loop and have not yet returned a value, we return $-1$.

Notice that we add $+1$ and $-1$, as we know that the value is not `med`.

## Complexity Analysis
- **Time Complexity**:  
  $O(\log n)$: The amount of work is halved at each step.
- **Space Complexity**:  
  $O(1)$: The number of variables are constant, and the variables themselves are constant aswell.
