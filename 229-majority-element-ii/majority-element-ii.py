class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        freq = Counter(nums)
        res = []
        for k , v in freq.items():
            if v > n // 3 :
                res.append(k)
        return res