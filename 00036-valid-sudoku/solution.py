from collections import defaultdict
from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # The number of fields horizontally/vertically in a board
        N = 9

        # The number of fields horizontally/vertically in a square (3x3)
        gridSize = 3


        # Initialize a HashMap of sets for the rows, the columns and the
        # squares
        rows = defaultdict(set)
        cols = defaultdict(set)
        square = defaultdict(set)

        # Iterate through each field
        for row in range(N):
            for col in range(N):
                # If there is no number in the field, we ignore this, as it
                # contributes nothing to the "validity".
                if board[row][col] == ".":
                    continue

                # The main logic. Check if the number has been seen before in
                # the same row or column or square, and if so return False
                if ((board[row][col] in rows[row]) or
                    (board[row][col] in cols[col]) or
                    (board[row][col] in
                     square[(row//gridSize, col//gridSize)])):
                    return False

                # Add the number to the respective row, column or square map.
                rows[row].add(board[row][col])
                cols[col].add(board[row][col])
                square[(row//gridSize, col//gridSize)].add(board[row][col])

        # If we get here, nothing has gone wrong and we can return True
        return True
