class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        hashmap = {}
        curr_sum = 0
        count = 0

        for i , v in enumerate(nums):
            curr_sum += v

            if curr_sum == k:
                count += 1
            
            if curr_sum - k in hashmap:
                count += hashmap[curr_sum - k]
            
            hashmap[curr_sum] = hashmap.get(curr_sum , 0) + 1
        
        return count