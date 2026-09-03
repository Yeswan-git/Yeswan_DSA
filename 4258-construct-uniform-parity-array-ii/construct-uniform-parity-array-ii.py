class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        min_num = min(nums1)
        if min_num % 2 != 0:
            return True
        return all(x % 2 == 0 for x in nums1)