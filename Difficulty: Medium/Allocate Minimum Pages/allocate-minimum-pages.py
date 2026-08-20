class Solution:
    def findPages(self, arr, k):
        if k > len(arr) : return -1
        def can_we_allocate(max_val):
            cnt = 1
            summ = 0
            for page in arr:
                if page > max_val: return False
                summ += page
                if summ > max_val :
                    cnt += 1
                    summ = page
            return cnt <= k
        
        l , r = min(arr) , sum(arr)
        res = -1
        while l <= r :
            mid = l + (r - l) // 2
            if can_we_allocate(mid):
                res = mid
                r = mid - 1
            else:
                l = mid + 1
        
        return res