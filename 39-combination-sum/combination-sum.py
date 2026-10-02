class Solution:
    def combinationSum(self, nums: list[int], target: int) -> list[list[int]]:
        n = len(nums)

        res , sol = [] , []

        def backtrack(i , curr_sum):
            if curr_sum == target:
                res.append(sol[:])
                return
            
            if curr_sum > target or i == n:
                return
            
            backtrack(i + 1 , curr_sum)

            sol.append(nums[i])
            backtrack(i , curr_sum + nums[i])
            sol.pop()
        
        backtrack(0 , 0)
        return res