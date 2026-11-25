class Solution:
    def countCommas(self, n: int) -> int:
        if n < 1000 : return 0
        count = 0
        limit = 1000
        while limit <= n :
            count += n - limit + 1
            limit *= 1000
        
        return count