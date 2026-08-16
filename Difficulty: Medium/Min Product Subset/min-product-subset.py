class Solution:
    def minProd(self, arr):
        neg_count = 0
        zero_count = 0
        prd = 1
        max_neg = float("-inf")
        min_pos = float("inf")
        
        for n in arr:
            if n < 0:
                neg_count += 1
                prd *= n
                max_neg = max(max_neg , n)
            elif n > 0:
                prd *= n
                min_pos = min(min_pos , n)
            else:
                zero_count += 1
        
        if not neg_count :
            if zero_count != 0 :
                return 0
            return min_pos
        
        if neg_count & 1:
            return prd
        else:
            return prd // max_neg