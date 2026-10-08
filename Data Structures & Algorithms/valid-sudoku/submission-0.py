class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = len(board[0])
        for col in range(n):
            row_set = set()
            col_set = set()
            for row in range(n):
                current_row = board[col][row]
                current_col = board[row][col]
                if current_row != '.':
                    if current_row in row_set:
                        return False
                    row_set.add(current_row)
                if current_col != '.':
                    if current_col in col_set:
                        return False
                    col_set.add(current_col)

        for box_col in range(0, 9, 3):
            for box_row in range(0, 9, 3):
                box_set = set()
                for row in range(box_row, box_row+3):
                    for col in range(box_col, box_col+3):
                        current = board[row][col]
                        if current != '.':
                            if current in box_set:
                                return False
                            box_set.add(current)

        return True
        