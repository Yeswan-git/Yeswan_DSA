class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        actual_sum = n * (n + 1) // 2

        array_sum = 0
        for e in nums:
            array_sum += e
        
        unique_sum = 0
        s = set(nums)
        for e in s:
            unique_sum += e
        
        miss = actual_sum - unique_sum
        dup = array_sum - unique_sum

        return [dup , miss]