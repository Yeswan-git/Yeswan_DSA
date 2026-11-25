class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        l , r = nums[0] , nums[1]
        nums[1] *= -1

        for i in range(2 , n):
            if l > r :
                l = nums[i]
            else:
                r = nums[i]
                nums[i] *= -1
        
        res = []
        for i in range(n):
            if nums[i] > 0:
                res.append(nums[i])
        for i in range(n):
            if nums[i] < 0 :
                res.append(-nums[i])
        
        return res