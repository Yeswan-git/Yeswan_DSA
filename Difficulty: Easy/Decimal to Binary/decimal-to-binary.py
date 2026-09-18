class Solution:
    def decToBinary(self, n):
        res = ""
        
        while n :
            res = str(n % 2) + res
            n //= 2
        
        return res