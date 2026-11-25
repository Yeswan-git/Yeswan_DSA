class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr_sum = 0
        max_sum = float("-inf")

        for i , v in enumerate(nums):
            curr_sum += v

            max_sum = max(max_sum , curr_sum)

            if curr_sum < 0 : curr_sum = 0
        
        return max_sum