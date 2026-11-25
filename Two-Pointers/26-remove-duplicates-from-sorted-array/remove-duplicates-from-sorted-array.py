class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        i = j = 1
        n = len(nums)

        while i < n :
            if nums[i] != nums[i - 1]:
                nums[j] = nums[i]
                j += 1


            i += 1
        return j