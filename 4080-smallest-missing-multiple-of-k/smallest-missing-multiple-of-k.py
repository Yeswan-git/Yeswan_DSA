class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        smallest = k
        m = 1

        while True :
            if smallest in nums :
                m += 1
                smallest = m * k
            
            else:
                return smallest
        