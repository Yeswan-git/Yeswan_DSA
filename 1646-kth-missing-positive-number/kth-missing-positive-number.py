class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        for n in arr:
            if n <= k : k += 1
            else : return k
        return k