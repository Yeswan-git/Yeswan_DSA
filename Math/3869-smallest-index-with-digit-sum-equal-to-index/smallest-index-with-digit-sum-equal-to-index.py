class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            d_sum = 0
            while nums[i]:
                d_sum += nums[i] % 10
                nums[i] //= 10
            if d_sum == i :
                return i
        return -1