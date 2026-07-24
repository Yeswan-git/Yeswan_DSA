class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(arr , low , mid , high):
            temp = []
            # [low ......... mid] , [mid + 1 .............. high]
            l , r = low , mid + 1
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
            for i in range(low , high + 1):
                arr[i] = temp[i - low]
        def ms(arr , low , high):
            if low == high:return
            mid = low + (high - low) // 2
            ms(arr , low , mid)
            ms(arr , mid + 1 , high)
            merge(arr , low , mid , high)
        ms(nums , 0 , len(nums) - 1)
        return nums