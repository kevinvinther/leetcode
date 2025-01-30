# Move Zeroes

## Problem Statement
<small>*(Briefly describe the problem, or copy the description from LeetCode in your own words.)*</small>

## Approach
1. **Idea**  
   Rather than thinking of the problem as moving 0's towards the end, we switch our thinking to be moving non-zeroes to the beginning.
   We use the two pointers approach, where our left pointer (writer), will continue untill it finds a 0, while the right pointer (reader) till continue untill it finds a non-zero.
2. **Steps/Pseudocode**  
   
We begin by initializing the left pointer to be 0. The right pointer will not be initialized, and instead we will use a for loop, which checks if the element at the index of `right` is equal to 0.

```python
left = 0

for right in range(len(nums)):
    if nums[right] != 0:
```

If the element is not zero, we swap, and increment `left` by one.

```python
        nums[left], nums[right] = nums[right], nums[left] # Swap
        left += 1
```

Finally, we return the array.

```python
return nums
```

## Complexity Analysis
- **Time Complexity**:  
  $O(n)$.
- **Space Complexity**:  
  $O(1)$: The given array was changed, and thus no new data structures were created.

