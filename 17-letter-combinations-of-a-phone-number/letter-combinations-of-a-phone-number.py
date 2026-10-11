class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        l_map = {'2' : "abc" , '3' : "def" , '4' : "ghi" , '5' : "jkl" , '6' : "mno" , '7' : "pqrs" , '8' : "tuv" , '9' : "wxyz"}

        res , sol = [] , []

        n = len(digits)

        def backtrack(i):
            if i == n : 
                res.append("".join(sol))
                return
            
            for letter in l_map[digits[i]]:
                sol.append(letter)
                backtrack(i + 1)
                sol.pop()
        
        backtrack(0)
        return res