class Solution:
    def aggressiveCows(self, arr, k):
        arr.sort()
        n = len(arr)
        def can_we_place(min_val):
            cow_cnt = 1
            last = arr[0]
            for i in range(1 , n):
                if arr[i] - last >= min_val :
                    cow_cnt += 1
                    last = arr[i]
            return cow_cnt >= k
            
        res = 1
        l , r = 1 , 10 ** 8
        while l <= r :
            mid = l + (r - l) // 2
            if can_we_place(mid) :
                res = mid
                l = mid + 1
            else:
                r = mid - 1
        return res