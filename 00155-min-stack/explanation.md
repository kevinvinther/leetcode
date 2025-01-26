# Min Stack

## Problem Statement
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

## Approach
1. **Idea**  
   The real problem here is in the "min" part. The way we do this is by having a seperate "min" stack from the normal stack. Then: 
   1. When pushing: We check if the newest addition to the min stack is larger than the value we're currently pushing. If so, we add it to the min stack.
   2. When popping: We check if the popped value is equal to the current top value in the min stack.
   As we are working with stacks, we cannot run into a scenario where a value later down the min stack has already been popped, as any smaller values must be popped beforehand.
2. **Steps/Pseudocode**  
   The steps can be found in the idea part. Pseudocode doesn't make sense for this.

## Complexity Analysis
- **Time Complexity**:  
  $O(1)$: All operations (push, pop, top, getMin) run in constant time.
- **Space Complexity**:  
  $O(n)$: The stacks hold all the values.
