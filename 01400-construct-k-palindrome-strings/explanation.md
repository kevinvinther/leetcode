# Construct K Palindrome Strings

## Problem Statement
Given a string $s$ and an integer $k$, return `true` if you can use all the characters in $s$ to construct $k$ palindrome strings, and `false` otherwise.

## Approach
1. **Idea**  
   Make the observation that if there are more odd occurrences of letters in the string than $k$, then it is not possible. Read more in Notes.
2. **Implementation**  
   1. Check first if the length of the string is smaller than $k$. If so, return `False`.
   2. Create a frequency dictionary for the string. (In Python this can be done using `Counter` from the `collections` library.)
   3. Add up the amount of odd values in the frequency dictionary.
   4. If the amount of odd values is less than or equal to $k$, it is possible, otherwise it is not.

## Complexity Analysis
- **Time Complexity**:  
  $O(n)$. Constructing the frequency dictionary takes $n$ steps. Going through the values takes $O(n)$ steps. 
- **Space Complexity**:  
  $O(n)$. The frequency dictionary is $O(n)$.

## Notes / Edge Cases
- **Elaboration on observation**
Given a string, for example 'leetcode', count each letter, and make a frequency dictionary. The result will look like this:
l = 1
e = 3
t = 1
c = 1
o = 1
d = 1
Now, given so many letters, it should seem intuitive that there are many possible palindromes. However, we notice that when we try to assemble together a palindrome with more than 3 characters, we fail. This is because the longest palindrome is 'eee'. If we insert any other, it "unbalances" the palindrome. However, if there were any even-numbered occurrences, we would be able to insert these with ease. 
Say the string with 'leetcoode' instead. Then we could construct the palindrome 'oeeeo'. The observation here, is that the least amount of palindromes we can create, is equal to the amount of odd-numbered frequencies.
