class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        res = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                res[j][n - i - 1] =  matrix[i][j]
        
        matrix[:] = res