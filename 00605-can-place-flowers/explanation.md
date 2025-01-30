# Can Place Flowers

## Problem Statement
You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.

Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return true if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule and false otherwise.

## Approach
### Idea
This problem is very simple, you just have to check all the cases before doing anything.
Since the flowerbed cannot have any flowers beside it, but it can be at the beginning or the end, it is not sufficient to check whether left and right is 0. Instead, you'll need to check off all these cases, before planting:
1. Is the current element at the index equal to 0? 
2. Is the current index 0 or the element before the current index 0?
3. Is the current index equal to the length of the flowerbed - 1 or the element after the current index 0? 

If you can check off "yes" to each of these, it is safe to plant a flower.

### Steps/Pseudocode

Rather than going through each line, I will focus on the code from the idea. 
We logic-ify the statements from the Idea section and get the following (python) code:
```python
flowerbed[i] == 0 and (i == 0 or flowerbed[i-1] == 0) and (i == len(flowerbed)-1 or flowerbed[i+1] == 0)
```
Here we check off all the cases from the Idea section.

Now, we do this for each element, and keep track of how many of these we can do, as well as actually modifying the flowerbed.

```python
flowers = 0

for i in range(len(flowerbed)):
    if flowerbed[i] == 0 and (i == 0 or flowerbed[i - 1] == 0) and (i == len(flowerbed) - 1 or flowerbed[i+1] == 0):
        flowers += 1
        flowerbed[i] = 1
```

Finally, we return if `flowers` is greater than or equal to the given `n`.

```python
return flowers >= n
```

## Complexity Analysis
- **Time Complexity**:  
  $O(n)$: We do constant work at each iteration. Assuming $n$ is the number of elements in `flowerbed`.
- **Space Complexity**:  
  $O(1)$: We have one additional variable, which is of constant space.

