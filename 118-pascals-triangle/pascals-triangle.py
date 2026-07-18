class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        def row_generator(n):
            row = []
            ans = 1
            row.append(ans)
            for i in range(1 , n):
                ans = ans * (n - i)
                ans = ans // i
                row.append(ans)
            return row
        

        res = []
        for i in range(1 , numRows + 1):
            res.append(row_generator(i))
        
        return res