class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        el1 = el2 = None
        cnt1 = cnt2 = 0

        for num in nums:
            if cnt1 == 0 and num != el2:
                el1 = num
                cnt1 = 1
            elif cnt2 == 0 and num != el1:
                el2 = num
                cnt2 = 1
            
            elif num == el1:
                cnt1 += 1
            elif num == el2:
                cnt2 += 1
            
            else:
                cnt1 -= 1
                cnt2 -= 1
        res = []
        cnt1 = cnt2 = 0
        for num in nums:
            if num == el1 : cnt1 += 1
            elif num == el2 : cnt2 += 1
        if cnt1 > n // 3 : res.append(el1)
        if cnt2 > n // 3 : res.append(el2)

        return res