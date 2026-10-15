class Solution:
    def jump(self, nums: list[int]) -> int:
        n = len(nums)

        end , far = 0 , 0

        smallest = 0

        for i in range(n - 1):
            far = max(far , nums[i] +i)

            if i == end:
                end = far
                smallest += 1
        
        return smallest
