class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        smallest = k
        m = 1
        new_nums = set(nums)
        while True :
            if smallest in new_nums :
                m += 1
                smallest = m * k
            
            else:
                return smallest
        