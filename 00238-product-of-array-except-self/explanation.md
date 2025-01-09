# Product of Array Except Self

## Problem Statement
Given an integer array, return an answer array where index $i$ is equal to the product of all the elements of the input array except the input array at integer $i$.

## Approach
1. The idea is to have three arrays: 
 1. $left$, which contains the cumulative product going from left to right of the input array.
 2. $right$, which contains the cumulative product going from right to left of the input array.
 3. $res$, the return array. The index $i$ in $res$ will be calculated by multiplying $left[i]$ and $right[i]$
2. Create the arrays, initialize each value to be zero, and the length to be equal to the length of nums.
3. Left: Set the first value to be one. Iterate over each value in nums, from the second value, and let the values of left be set as: `left[i] = left[i-1] * nums[i-1]`.
4. Right: Set the first value to be one. Iterate over each value in nums, from the second to last value, and let the values of right be set as: `right[i] = right[i+1] * nums[i+1]`.
5. To save runtime, use the same loop for the right array to calculate the $res$ array: `res[i] = left[i] * right[i]`.
6. This leaves out the last value of $res$, so we set this explicitly, outside the loop.
7. Return $res$.

## Complexity Analysis
- **Time Complexity**:  
  $O(n)$. We loop over $nums$ twice.
- **Space Complexity**:  
  $O(n)$. We have three arrays of size $n$.

## Notes / Edge Cases
- It is possible to make a solution which uses $O(1)$ space complexity. This is not explored here.
