# Increasing Triplet Subsequence

## Problem Statement
Given an integer array nums, return true if there exists a triple of indices (i, j, k) such that i < j < k and nums[i] < nums[j] < nums[k]. If no such indices exists, return false.

## Approach
### Idea
This problem is very easy, when you understand what you have to do. The only thing you need to see, is *if*, given a sequence, there exists a subsequence $i < j < k \text{ and } nums[i] < nums[j] < nums[k]$ where $i,j,k$ are indices. We can very simply check this, by creating two variables with an infinitely high value. Then we go through the array, and first check if any value is smaller than the first variable. Given $n > 1$, the answer *will* be yes. Then, we check using an else if, if a number is smaller than the next variable. Lastly, if the number is neither smaller than the first variable nor the second variable, it is larger, and thus we can conclude that the sequence exists.

### Steps/Pseudocode
```python
small = float('inf')
big = float('inf')

for num in nums:
  if num <= small:
      small = num
  elif num <= big:
      big = num
  else:
      return True

return False
```

Notice that we return `false` in case we never get to the `else` statement, as this means that there is no such sequence.

## Complexity Analysis
- **Time Complexity**:  
  $O(n)$.
- **Space Complexity**:  
  $O(1)$: The variables are of constant size.
