class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        if not matrix:
            return res
        
        # Initialize boundaries
        left, right = 0, len(matrix[0])
        top, bottom = 0, len(matrix)
        
        while left < right and top < bottom:
            # 1. Get every i in the top row
            for i in range(left, right):
                res.append(matrix[top][i])
            top += 1
            
            # 2. Get every i in the right column
            for i in range(top, bottom):
                res.append(matrix[i][right - 1])
            right -= 1
            
            # Check if we finished the matrix (for non-square matrices)
            if not (left < right and top < bottom):
                break
                
            # 3. Get every i in the bottom row (reverse)
            for i in range(right - 1, left - 1, -1):
                res.append(matrix[bottom - 1][i])
            bottom -= 1
            
            # 4. Get every i in the left column (reverse)
            for i in range(bottom - 1, top - 1, -1):
                res.append(matrix[i][left])
            left += 1
            
        return res
