# Two Sum

## Problem Statement
Given a target number and a list of numbers, return the two distinct indices whose corresponding number add up to the target.

## Approach
1. Make the observation that `target = num1 + num2` can be rearranged to `num1 = target - num2`, call this the complement.
2. Create a HashMap. This will contain as a key the complement and as value the index.
3. For each number in the list of numbers
    - Calculate it's component
    - Check if the complement is a key yet. 
        - If Yes: Return the value in the hashmap, as well as the current index.
        - If No: Add the current number as a key in the hashmap, and the index as corresponding value.

## Complexity Analysis
- **Time Complexity**:  
  $O(n)$. You only make one pass-through on the numbers list, and the rest is constant time.
- **Space Complexity**:  
  $O(n)$. You only create one new data structure: The hashmap, which can take upon it all $n$ numbers.

## Further Thoughts 
A way more intuitive way to do this, would be by using nesting for loops. However, this would result in $O(n^2)$ running time.
