# String Compression

## Problem Statement
Given an array of characters chars, compress it using the following algorithm:

Begin with an empty string s. For each group of consecutive repeating characters in chars:

* If the group's length is 1, append the character to s.
* Otherwise, append the character followed by the group's length.

The compressed string s should not be returned separately, but instead, be stored in the input character array chars. Note that group lengths that are 10 or longer will be split into multiple characters in chars.

After you are done modifying the input array, return the new length of the array.

## Approach
1. **Idea**  
   The idea is pretty straight forward. We keep track of the current "group size", i.e. the amount of consecutive letters, as well as the "index", which keeps track of where in the array we are.
2. **Steps/Pseudocode**  
Initialize `index` and `res` to be 0.
```python
index = 0
res = 0
```

While `index` is less than the length of the input array.
```python
while index < len(chars):
```

Initialize a new variable, `group_size` and set it to 0.
```python
    group_size = 0
```

Now, while `index + group_size` is less than the length of the input array, *and* while the char at the index `index` is equal to `index + group_size`, increment the `group_size` by one. That is, keep incrementing `group_size` by one while the next character is the same as the one that begins the group. Thus we get a `group_size` that increments until the end of the group.
```python
    while index + group_size < len(chars) and chars[index] == chars[index + group_size]:
        group_size += 1
```

Now set the character at the index of `res` to be equal to the character at the index of `index`. This is because, after one or more groups, the character at `res` is unlikely to be the correct character. Furthermore, increment `res` by one.
```python
    chars[res] = chars[index]
    res += 1
```


Now, if `group_size` is above 1, we have to add the amount to the array, therefore we do the following: 
1. Convert `group_size` to a string
2. Get the length of the string
3. At the index of `res` until `res + length(group_size_string)` we set this to be the `group_size` string. It's done like this for numbers > 9.
4. Last, we add the length of group_size to res, in order to let it go past the group.

```python
    if group_size > 1:
        s = str(group_size)
        l = len(s)
        chars[res:res+l] = s
        res += l
```


Then we increment `index` by `group_size` because we need to get to the next character.
```python
    index += group_size
```

Finally, we return `res`:
```python
return res
```


## Complexity Analysis
- **Time Complexity**:  
  $O(n)$: Through each character, we do constant work.
- **Space Complexity**:  
  $O(1)$: All variables are of constant space, including `group_size`, and the string conversion.

## Notes / Edge Cases
- <small>*(List any edge cases or special considerations.)*</small>

## Further Thoughts (Optional)
<small>*(Discuss alternative solutions, optimizations, or any insights learned.)*</small>
