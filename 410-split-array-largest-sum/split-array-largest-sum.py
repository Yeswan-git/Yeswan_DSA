class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def helper(max_val):
            splits = 1
            summ = 0
            for num in nums:
                if num > max_val : return False
                summ += num
                if summ > max_val :
                    splits += 1
                    summ = num
            return splits <= k
        
        l , r = max(nums) , sum(nums)
        res = r

        while l <= r :
            mid = l + (r - l) // 2
            if helper(mid) :
                res = mid 
                r = mid - 1
            else:
                l = mid + 1
        
        return res