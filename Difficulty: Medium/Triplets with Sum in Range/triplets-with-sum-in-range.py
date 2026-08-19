class Solution:
    def countTriplets(self, arr: list[int], l: int, r: int) -> int:
        arr.sort()
        
        def count_less_than(arr , val):
            n = len(arr)
            cnt = 0
            for i in range(n - 2):
                left , right = i + 1 , n - 1
                while left < right:
                    summ = arr[i] + arr[left] + arr[right]
                    if summ <= val:
                        cnt += (right - left)
                        left += 1
                    else:
                        right -= 1
            return cnt
        return count_less_than(arr , r) - count_less_than(arr , l - 1)