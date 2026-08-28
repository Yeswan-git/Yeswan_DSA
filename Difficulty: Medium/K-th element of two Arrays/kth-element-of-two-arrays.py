class Solution:
    def kthElement(self, a, b, k):
        n1 , n2 = len(a) , len(b)
        n = n1 + n2
        if n1 > n2 : return self.kthElement(b , a , k)
        left = k
        l , r = max(0 , k - n2) , min(k , n1)
        
        while l <= r :
            mid1 = (l + r) >> 1
            mid2 = left - mid1
            l1 = l2 = float("-inf")
            r1 = r2 = float("inf")
            if mid1 - 1 >= 0 : l1 = a[mid1 - 1]
            if mid2 - 1 >= 0 : l2 = b[mid2 - 1]
            if mid1 < n1 : r1 = a[mid1]
            if mid2 < n2 : r2 = b[mid2]
            
            if l1 <= r2 and l2 <= r1 :
                return max(l1 , l2)
            
            elif l1 > r2 :
                r = mid1 - 1
            
            else :
                l = mid1 + 1
                