class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        el = 0
        cnt = 0

        for e in nums:
            if cnt == 0:
                el = e
                cnt = 1
            elif el != e:
                cnt -= 1
            elif el == e:
                cnt += 1

            if cnt > n // 2:
                return el
        return el