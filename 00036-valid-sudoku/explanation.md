# Valid Sudoku

## Problem Statement
Given a board of 9x9 fields, check if the board is a valid Sudoku board. It does not need to be solvable, but each number should only appear once in each row, column and 3x3 square.

## Approach
1. Make the observation that each square can be indexed by a pair where the row and column has been divided by three and rounded down: $(\lfloor row / 3 \rfloor, \lfloor col / 3 \rfloor)$.
2. Create hashmaps initialized with sets for each place where there cannot be more than one of each number (rows, columns, squares).
3. Go through each field
 - Check if the field is a number, if not, go to the next iteration.
 - Check if the field as already been seen in one of the maps. If it has, return False.
 - With the key being the current row, column or square, add to the set the current number. 
4. If nothing has gone wrong, the Sudoku is valid, thus return true.

## Complexity Analysis
- **Time Complexity**:  
  $O(n^2)$: Asssuming $n$ is 9. We repeat the for loop inside the for loop.
- **Space Complexity**:  
  $O(n)$: Three hashmaps, each holding up to 9 digits, and each holding 9 sets. 
