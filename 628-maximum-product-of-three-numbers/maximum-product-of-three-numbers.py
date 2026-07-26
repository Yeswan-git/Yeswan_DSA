class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        max1 = max2 = max3 = float("-inf")
        min1 = min2 = float("inf")

        for n in nums:
            # three maximum values 
            if n > max1:
                max3 = max2
                max2 = max1
                max1 = n
            elif n > max2:
                max3 = max2
                max2 = n
            elif n > max3:
                max3 = n
            
            # two minimum values
            
            if n < min1:
                min2 = min1
                min1 = n
            elif n < min2:
                min2 = n
            
        return max(max1 * max2 * max3 , min1 * min2 * max1)