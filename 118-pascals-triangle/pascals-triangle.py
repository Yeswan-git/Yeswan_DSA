class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        def row_generator(n):
            row = [1]
            ans = 1
            for i in range(1 , n):
                ans *= (n - i)
                ans //= i
                row.append(ans)
            return row
        

        res = []
        for i in range(1 , numRows + 1):
            res.append(row_generator(i))
        
        return res