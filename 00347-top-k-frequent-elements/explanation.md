# Top K Frequent Elements

## Problem Statement
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

## Approach
### Idea
   In order to achieve a *linear* time complexity, we use a version of _Bucket Sort_. We will do this by using an array that at index $i$ contains the element which occurs $i$ times. That way, we can traverse backwards until we have the $k$ most frequent elements.

### Steps

First we initialize a hashmap, and a frequency map. The hashmap will function as a "frequency dictionary", where we count the frequency of each element in the array.
```python
map = {}
freq = [[] for i in range(len(nums)+1)]
```

We then populate the hash map, such that the key is the value of the element in the array, and the value is the frequency of the key.
 
```python
for i in nums:
    map[i] = map.get(i, 0) + 1
```

Then we populate the frequency list:

```python
for key, value in map.items():
    freq[value].append(key)
```

Finally, we build up the result array, which contains the $k$ most frequent elements in the array, and return $-1$, if this is not possible.

Notice that `for y in freq[i]` appears, as there may be more than one element with the frequency $i$.

```python
res = []
for i in range(len(nums), 0, -1):
    for y in freq[i]:
        res.append(y)
        if len(res) == k:
            return res
return -1
```




## Complexity Analysis
- **Time Complexity**:  
  $O(n)$.
- **Space Complexity**:  
  $O(n)$: The hash map, array and `res` each are of $O(n)$ size.

