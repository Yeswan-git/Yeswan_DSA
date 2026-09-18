class Solution:
    def countGoodNumbers(self, n: int) -> int:
        MOD = 10 ** 9 + 7
        def Pow(x , n):
            res = 1
            x %= MOD

            while n :
                if n & 1 :
                    res = (res * x) % MOD
                
                x = (x * x) % MOD
                n = n // 2
            
            return res % MOD
        
        even_idxs = (n + 1) // 2
        odd_idxs = n - even_idxs

        return (Pow(5 , even_idxs) * Pow(4 , odd_idxs)) % MOD
        