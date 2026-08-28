class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in range(len(matrix)):
            row = matrix[i]
            l , r = 0 , len(row) - 1
            while l <= r:
                mid = l + (r - l) // 2
                if row[mid] == target:
                    return True
                elif row[mid] > target:
                    r = mid - 1
                else:
                    l = mid + 1
        return False
