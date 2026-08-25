class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        multiple = k
        nums_set = set(nums)

        while multiple in nums_set :
            multiple += k
        
        return multiple