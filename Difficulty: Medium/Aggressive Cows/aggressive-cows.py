class Solution:
    def aggressiveCows(self, arr, k):
        arr.sort()
        n = len(arr)
        def can_we_place(min_dist):
            cnt_cows = 1
            last = arr[0]
            for i in range(1 , n):
                if arr[i] - last >= min_dist:
                    cnt_cows += 1
                    last = arr[i]
            return cnt_cows >= k
        l , r = 1 , max(arr) - min(arr)
        res = 1
        while l <= r :
            mid = l + (r - l) // 2
            if can_we_place(mid):
                res = mid
                l = mid + 1
            else:
                r = mid - 1
        return res