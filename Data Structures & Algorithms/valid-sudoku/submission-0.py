class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        r = 9
        c = 9   

        def check_cols(board):
            i = 0
            for col in range(c):
                seen = set()
                for row in range(r): 
                    cur = board[row][col]
                    if cur == '.':
                        continue
                    if cur not in seen:
                        seen.add(cur)
                    else:
                        return False
            return True 
        
        def check_rows(board):
            i = 0
            for row in range(r):
                seen = set()
                for col in range(c):
                    cur = board[row][col]
                    if cur == '.':
                        continue
                    if cur not in seen:
                        seen.add(cur)
                    else:
                        return False
            return True 
        def check_square(board):
            i = 0
            seen = set()

        def check_square(board):
            for box_row in range(0, 9, 3):
                for box_col in range(0, 9, 3):
                    seen = set()
                    for row in range(box_row, box_row + 3):
                        for col in range(box_col, box_col + 3):
                            cur = board[row][col]
                            if cur == '.':
                                continue
                            if cur in seen:
                                return False
                            seen.add(cur)
            return True


        return all([check_rows(board), check_cols(board), check_square(board)])
