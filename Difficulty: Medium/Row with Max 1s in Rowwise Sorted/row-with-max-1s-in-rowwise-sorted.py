class Solution:
    def rowWithMax1s(self, arr: list[list[int]]) -> int:
        m , n = len(arr) , len(arr[0])
        ans = -1
        max_ones = 0
        for i in range(m):
            row = arr[i]
            l , r = 0 , n - 1
            idx = -1
            while l <= r:
                mid = (l + r) >> 1
                if row[mid]:
                    idx = mid
                    r = mid - 1
                else:
                    l = mid + 1
            ones = n - idx if idx != -1 else 0
            if ones > max_ones : 
                ans = i
                max_ones = ones
        return ans