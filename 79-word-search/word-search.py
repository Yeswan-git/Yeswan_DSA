class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        rows , cols = len(board) , len(board[0])
        w = len(word)

        if rows == 1 and cols == 1 :
            return board[0][0] == word
        def backtrack(pos , index):
            i , j = pos

            if index == w:
                return True
            
            if board[i][j] != word[index]:
                return False
            
            char = board[i][j]
            board[i][j] = "$"
            for i_off , j_off in [(1 , 0) , (0 , 1) , (0 , -1) , (-1 , 0)]:
                r , c = i + i_off , j + j_off
                if 0 <= r < rows and 0 <= c < cols:
                    if backtrack((r , c) , index + 1):
                        return True
            
            board[i][j] = char
            return False

        

        for i in range(rows):
            for j in range(cols):
                if backtrack((i , j) , 0):
                    return True
        
        return False