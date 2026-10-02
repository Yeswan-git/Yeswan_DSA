class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        n = len(nums)
        res , sol = [] , []
        def backtrack(i):
            if i >= n:
                res.append(sol[:])
                return
            
            # not pick
            backtrack(i + 1)

            # pick
            sol.append(nums[i])
            backtrack(i + 1)
            sol.pop()
        
        backtrack(0)
        return res