class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        sm = min(nums)
        lar = max(nums)
        present = set(nums)
        res = []
        for i  in range(sm,lar+1):
            if i not in present:
                res.append(i)
        return res