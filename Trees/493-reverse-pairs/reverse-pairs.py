class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        count = [0] 
        def merge(arr, low, mid, high):
            temp = []
            # [low ............ mid] , [mid + 1 .......... high]
            l, r = low, mid + 1
            while l <= mid and r <= high:
                if arr[l] > 2 * arr[r]:
                    count[0] += mid - l + 1  
                    r += 1
                else:
                    l += 1
            
            l, r = low, mid + 1
            while l <= mid and r <= high:
                if arr[l] <= arr[r]:
                    temp.append(arr[l])
                    l += 1
                else:
                    temp.append(arr[r])
                    r += 1
            while l <= mid:
                temp.append(arr[l])
                l += 1
            while r <= high:
                temp.append(arr[r])
                r += 1
            arr[low : high + 1] = temp
        
        def ms(arr, low, high):
            if low == high:
                return
            mid = low + (high - low) // 2
            ms(arr, low, mid)
            ms(arr, mid + 1, high)
            merge(arr, low, mid, high)
        
        copy = nums
        ms(nums, 0, len(nums) - 1)
        return count[0]