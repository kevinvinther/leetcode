# [Problem Title]

## Problem Statement
Return the concatenation of an array, into an array of double lenght, where $n$ is the size of the array and $arr[i+n] = arr[i]$.

## Approach
1. This can be done very easily in python simply using $+$: `return nums + nums`. 
2. In case you don't use python, create a new array double the size of $nums$. Iterate through $nums$, adding each value to the new array. After this is done, iterate through nums again, adding again, but from the end of the new array.

## Complexity Analysis
- **Time Complexity**:  
  $O(n)$. Concatenation takes $n$ time, as you have to copy each
- **Space Complexity**:  
  $O(n)$. The new array takes $2n$ space.

