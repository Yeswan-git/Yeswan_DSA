class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        return sum(nums[i - 1] ** 2 for i in range(1 , len(nums) + 1) if len(nums) % i == 0)
