class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n1 , n2 = len(nums1) , len(nums2)
        nums = []
        i = j = 0
        while i < n1 and j < n2:
            if nums1[i] <= nums2[j]:
                nums.append(nums1[i])
                i += 1
            else:
                nums.append(nums2[j])
                j += 1
        while i < n1:
            nums.append(nums1[i])
            i += 1
        while j < n2:
            nums.append(nums2[j])
            j += 1
        
        n = n1 + n2
        if n % 2 == 0:
            index = (n - 1) // 2
            n1 = nums[index]
            n2 = nums[index + 1]
            median = (n1 + n2) / 2
        else:
            median = nums[n // 2]

        return median


        