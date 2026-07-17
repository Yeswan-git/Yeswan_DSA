class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows , cols = len(matrix) , len(matrix[0])
        zeros = []

        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == 0:
                    zeros.append((r , c))
            
        for r , c in zeros:

            for k in range(rows):
                matrix[k][c] = 0
            
            for k in range(cols):
                matrix[r][k] = 0