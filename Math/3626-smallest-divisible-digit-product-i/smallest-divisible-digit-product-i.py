class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        for i in range(n , 100):
            p = 1
            temp = i
            while i:
                p *= i % 10
                i //= 10
            if p % t == 0:
                return temp
        return 100