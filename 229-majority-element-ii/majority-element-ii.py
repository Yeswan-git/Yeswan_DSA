class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        el1 = el2 = None
        cnt1 = cnt2 = 0
        length = len(nums)
        for n in nums:
            if cnt1 == 0 and n != el2:
                el1 = n
                cnt1 = 1
            elif cnt2 == 0 and n != el1:
                el2 = n
                cnt2 = 1
            elif n == el1:
                cnt1 += 1
            elif n == el2:
                cnt2 += 1
            else:
                cnt1 -= 1
                cnt2 -= 1
        
        count1 = count2 = 0
        for n in nums:
            if n == el1:
                count1 += 1
            elif n == el2:
                count2 += 1
        res = []
        if count1 > length // 3:
            res.append(el1)
        if count2 > length // 3:
            res.append(el2)
        return res