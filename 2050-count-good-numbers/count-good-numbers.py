class Solution:
    def countGoodNumbers(self, n: int) -> int:
        MOD = 10 ** 9 + 7

        def Pow(base , exp):
            res = 1
            base %= MOD

            while exp :
                if exp & 1 :
                    res = (res * base) % MOD
                
                base = (base * base) % MOD
                exp = exp // 2
            
            return res % MOD
        
        even_idxs = (n + 1) // 2
        odd_idxs = n - even_idxs

        return (Pow(5 , even_idxs) * Pow(4 , odd_idxs)) % MOD