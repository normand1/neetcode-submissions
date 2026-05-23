class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        ROWS = len(matrix)
        COLS = len(matrix[0])

        # iterate over the matrix from top to bottom to find the row
        TOP = 0
        BOTTOM = ROWS - 1

        while TOP <= BOTTOM:

            mid_row = (TOP + BOTTOM) // 2
            if matrix[mid_row][0] <= target <= matrix[mid_row][-1]:
                # mid_row is where the target is
                break
            elif matrix[mid_row][-1] > target:
                BOTTOM = mid_row - 1
            else:
                TOP = mid_row + 1
        
        if not TOP <= BOTTOM:
            return False
        
        # iterate over the matrix from left to right to find the col of the answer

        mid_row = (TOP + BOTTOM) // 2
        print(mid_row)

        l = 0
        r = len(matrix[0]) - 1

        while l <= r:
            mid = (l + r) // 2

            if target == matrix[mid_row][mid]:
                return True
            elif target > matrix[mid_row][mid]:
                l = mid + 1
            else:
                r = mid - 1
        
        return False

                

