class Solution:
    def countGoodNumbers(self, n: int) -> int:
        MOD = 10**9 + 7
        even_idxs = (n + 1) // 2
        odd_idxs = n // 2
        
        return (pow(5, even_idxs, MOD) * pow(4, odd_idxs, MOD)) % MOD