class Solution:
    def minMaxDist(self, arr , k):
        from math import ceil
        n = len(arr)
        l = 0.0
        r = 0.0
        for i in range(n - 1):
            r = max(r , arr[i + 1] - arr[i])
        
        def can_we_place(max_val):
            placed = 0
            for i in range(n - 1):
                gap = arr[i + 1] - arr[i]
                placed += ceil(gap / max_val) - 1
            return placed <= k
                
                
        
        res = r
        while r - l > 10 ** -6:
            mid = l + (r - l) / 2
            if can_we_place(mid):
                res = mid
                r = mid
            else:
                l = mid
        
        return res