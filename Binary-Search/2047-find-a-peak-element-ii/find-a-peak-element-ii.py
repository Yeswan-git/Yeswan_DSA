class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        def max_row_index(mat , rows , mid):
            maxx = -1
            idx = -1
            for r in range(rows):
                if maxx < mat[r][mid]:
                    maxx = mat[r][mid]
                    idx = r
            return idx

        rows , cols = len(mat) , len(mat[0])
        l , r = 0 , cols - 1

        while l <= r :
            mid = (l + r) >> 1
            row = max_row_index(mat , rows , mid)
            left = mat[row][mid - 1] if mid - 1 >= 0 else -1
            right = mat[row][mid + 1] if mid + 1 < cols else -1

            if left < mat[row][mid] > right :
                return [row , mid]
            
            elif left  > mat[row][mid] : 
                r = mid - 1
            
            else :
                l = mid + 1
        

        return [-1 , -1]