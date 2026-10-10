class Solution:
    def combinationSum3(self, k: int, n: int) -> list[list[int]]:
        res , sol = [] , []

        def backtrack(i , curr_sum):
            if curr_sum == n + 1 and len(sol) == k:
                res.append(sol[:])
                return
            
            if curr_sum > n or i == 10:
                return
            
            backtrack(i + 1 , curr_sum)

            sol.append(i)
            backtrack(i + 1 , curr_sum + i)
            sol.pop()
        
        backtrack(1 , 1)
        return res