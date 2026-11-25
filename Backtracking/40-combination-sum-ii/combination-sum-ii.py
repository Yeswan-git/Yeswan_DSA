class Solution:
    def combinationSum2(self, nums: list[int], target: int) -> list[list[int]]:
        nums.sort()
        n = len(nums)
        res , sol = [] , []

        def backtrack(i , curr_sum):
            if curr_sum == target:
                res.append(sol[:])
                return

            if curr_sum > target or i == n:
                return
            

            sol.append(nums[i])
            backtrack(i + 1 , curr_sum + nums[i])
            sol.pop()

            j = i
            while j < n and nums[j] == nums[i]:
                j += 1
            
            backtrack(j , curr_sum)
        
        backtrack(0 , 0)
        return res