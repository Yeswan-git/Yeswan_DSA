class Solution:
    def maxProduct(self, n: int) -> int:
        maxx1 = maxx2 = 0

        while n :
            d = n % 10
            if d >= maxx1:
                maxx2 = maxx1
                maxx1 = d
            elif d > maxx2:
                maxx2 = d
            n //= 10
        
        return maxx1 * maxx2