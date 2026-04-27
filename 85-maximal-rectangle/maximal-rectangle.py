class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        
        cols = len(matrix[0])
        heights = [0] * (cols + 1) # Extra 0 at end to flush the stack
        max_area = 0
        
        for row in matrix:
            # Update heights for the current row
            for i in range(cols):
                heights[i] = heights[i] + 1 if row[i] == "1" else 0
            
            # Find largest rectangle in the current histogram (row)
            stack = [-1]
            for i in range(len(heights)):
                while heights[i] < heights[stack[-1]]:
                    h = heights[stack.pop()]
                    w = i - stack[-1] - 1
                    max_area = max(max_area, h * w)
                stack.append(i)
                
        return max_area
