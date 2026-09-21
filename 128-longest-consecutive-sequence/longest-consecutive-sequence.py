class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        n = len(nums)
        nums_set = set(nums)
        longest = 0
        for num in nums_set :
            if num - 1 in nums_set :
                continue
            
            next_num = num + 1
            curr_len = 1
            while next_num in nums_set :
                curr_len += 1
                next_num += 1
            
            longest = max(longest , curr_len)
        
        return longest