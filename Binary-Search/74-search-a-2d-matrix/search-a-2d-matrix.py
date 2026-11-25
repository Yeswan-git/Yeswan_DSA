class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row , col = len(matrix) , len(matrix[0])
        l , r = 0 , row * col - 1
        
        while l <= r :
            mid = (l + r) >> 1
            i = mid // col
            j = mid % col
            if matrix[i][j] == target :
                return True
            
            elif matrix[i][j] < target :
                l = mid + 1
            
            else :
                r = mid - 1
        
        return False