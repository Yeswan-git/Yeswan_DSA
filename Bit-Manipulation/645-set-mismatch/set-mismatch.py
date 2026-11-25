class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        actual_sum = n * (n + 1) // 2
        arr_sum = sum(n for n in nums)
        unique_sum = sum(n for n in set(nums))
        return [arr_sum - unique_sum , actual_sum - unique_sum]