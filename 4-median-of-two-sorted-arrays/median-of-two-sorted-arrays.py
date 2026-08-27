class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n1 , n2 = len(nums1) , len(nums2)
        n = n1 + n2

        idx1 = n // 2 - 1
        idx2 = n // 2
        cnt = 0
        el1 = el2 = -1
        i = j = 0
        while i < n1 and j < n2 :
            if nums1[i] <= nums2[j]:
                if cnt == idx1 : el1 = nums1[i]
                if cnt == idx2 : el2 = nums1[i]
                cnt += 1
                i += 1
            else:
                if cnt == idx1 : el1 = nums2[j]
                if cnt == idx2 : el2 = nums2[j]
                cnt += 1
                j += 1
            if el1 != -1 and el2 != -1 : break
        
        while i < n1 :
            if cnt == idx1 : el1 = nums1[i]
            if cnt == idx2 : el2 = nums1[i]
            cnt += 1
            i += 1
            if el1 != -1 and el2 != -1 : break
        while j < n2 :
            if cnt == idx1 : el1 = nums2[j]
            if cnt == idx2 : el2 = nums2[j]
            cnt += 1
            j += 1
            if el1 != -1 and el2 != -1 : break
        
        if n & 1 : return el2
        else : return (el1 + el2) / 2