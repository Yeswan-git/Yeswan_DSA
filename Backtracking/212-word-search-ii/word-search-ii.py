class Solution:
    def findWords(self, board: list[list[str]], words: list[str]) -> list[str]:
        class TrieNode:
            def __init__(self):
                self.children = {}
                self.endOfWord = False

        class Trie:
            def __init__(self):
                self.root = TrieNode()

            def insert(self, word: str) -> None:
                curr = self.root
                for c in word:
                    if c not in curr.children:
                        curr.children[c] = TrieNode()
                    curr = curr.children[c]
                curr.endOfWord = True
        
        root = Trie()
        for word in words:
            root.insert(word)
        
        res = set()
        rows , cols = len(board) , len(board[0])

        def backtrack(i , j , st , curr):
            letter = board[i][j]

            if letter not in curr.children:
                return
            
            curr = curr.children[letter]
            st += letter

            if curr.endOfWord:
                res.add(st)
            
            board[i][j] = "$"

            for i_off , j_off in [(0 , 1) , (1 , 0) , (0 , -1) , (-1 , 0)]:
                r , c = i + i_off , j + j_off
                if 0 <= r < rows and 0 <= c < cols and board[r][c] != "#":
                    backtrack(r , c, st , curr)
            
            board[i][j] = letter
        
        for i in range(rows):
            for j in range(cols):
                backtrack(i , j , "" , root.root)
        
        return list(res)