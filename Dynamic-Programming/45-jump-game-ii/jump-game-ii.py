class Solution:
    def jump(self, nums: list[int]) -> int:
        n = len(nums)
        end , far = 0 , 0 
        smallest = 0

        for i in range(n - 1):
            far = max(nums[i] + i , far)

            if i == end:
                smallest += 1
                end = far
        
        return smallest