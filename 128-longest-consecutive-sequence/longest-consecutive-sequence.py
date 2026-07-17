class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        max_len = 0
        for num in s:
            if num - 1 not in s:
                length = 1
                next_number = num + 1
                while next_number in s:
                    length += 1
                    next_number += 1
                max_len = max(max_len , length)
        return max_len