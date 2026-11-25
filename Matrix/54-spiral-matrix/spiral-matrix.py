class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        r , c = len(matrix) , len(matrix[0])
        ans = []
        top_wall = 0
        right_wall = c - 1
        down_wall = r - 1
        left_wall = 0
        direction = "right"
        i = j = 0
        while r * c != len(ans):
            if direction == "right":
                while j <= right_wall:
                    ans.append(matrix[i][j])
                    j += 1
                i , j = i + 1 , j - 1
                right_wall -= 1
                direction = "down"

            elif direction == "down":
                while i <= down_wall:
                    ans.append(matrix[i][j])
                    i += 1
                i , j = i - 1 , j - 1
                down_wall -= 1
                direction = "left"
            
            elif direction == "left":
                while j >= left_wall:
                    ans.append(matrix[i][j])
                    j -= 1
                i , j = i - 1 , j + 1
                left_wall += 1
                direction = "top"

            elif direction == "top":
                while i > top_wall:
                    ans.append(matrix[i][j])
                    i -= 1
                i , j = i + 1 , j + 1
                top_wall += 1
                direction = "right"

        return ans