class Solution:
    def minTime (self, arr, k):
        def helper(max_val):
            painter = 1
            painted = 0
            for area in arr :
                if area > max_val : return False
                painted += area
                if painted > max_val:
                    painter += 1
                    painted = area
            return painter <= k
        l , r = max(arr) , sum(arr)
        res = r
        while l <= r :
            mid = l + (r - l) // 2
            if helper(mid):
                res = mid
                r = mid - 1
            else:
                l = mid + 1
        
        return res