class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)
        maxs = [0] * n
        maxs[0] = nums[0]
        mins = [0] * n
        mins[n - 1] = nums[n - 1]
        for i in range(1 , n):
            maxs[i] = max(maxs[i - 1] , nums[i])
            mins[n - i - 1] = min(mins[n - i] , nums[n - i - 1])
        
        for i in range(n):
            if maxs[i] - mins[i] <= k :
                return i
        
        return -1