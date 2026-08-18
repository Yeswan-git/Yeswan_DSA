class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        if k < arr[0] : return k
        n = len(arr)
        if k > arr[n - 1] : return n + k
        l , r = 0 , n - 1
        while l <= r:
            mid = l + (r - l) // 2
            miss = arr[mid] - (mid + 1)
            if miss < k:
                l = mid + 1
            else:
                r = mid - 1
        miss_at_r = arr[r] - (r + 1)
        return arr[r] + (k - miss_at_r)