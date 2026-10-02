class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        res , sol = [] , []

        def backtrack(openn , close):
            if len(sol) == 2 * n:
                res.append("".join(sol))
                return
            
            if openn < n :
                sol.append("(")
                backtrack(openn + 1 , close)
                sol.pop()
            
            if openn > close:
                sol.append(")")
                backtrack(openn , close + 1)
                sol.pop()
        
        backtrack(0 , 0)
        return res