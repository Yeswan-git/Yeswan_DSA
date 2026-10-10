class Solution:
    def combinationSum(self, nums: list[int], target: int) -> list[list[int]]:
        res , sol = [] , []
        curr_sum = 0
        n = len(nums)
        def backtrack(i , curr_sum):
            if i == n or curr_sum > target:
                return
            
            if curr_sum == target:
                res.append(sol[:])
                return
            
            sol.append(nums[i])
            backtrack(i , curr_sum + nums[i])
            sol.pop()

            backtrack(i + 1 , curr_sum)
        
        backtrack(0 , 0)
        return res
