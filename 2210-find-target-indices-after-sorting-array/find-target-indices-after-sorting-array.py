class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        count_less = sum(num < target for num in nums)
        count_eq = sum(num == target for num in nums)
        return [count_less + i for i in range(count_eq)]