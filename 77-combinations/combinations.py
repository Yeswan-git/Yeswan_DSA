class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        res , sol = [] , []

        def backtrack(x):
            if len(sol) == k:
                res.append(sol[:])
                return
            if x == 0 :
                return
            
            backtrack(x - 1)
            
            sol.append(x)
            backtrack(x - 1)
            sol.pop()
            
            
        backtrack(n)
        return res