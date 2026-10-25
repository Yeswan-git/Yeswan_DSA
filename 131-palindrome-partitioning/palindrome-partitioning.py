class Solution:
    def partition(self, s: str) -> list[list[str]]:
        n = len(s)
        res , sol = [] , []
        def isPalindrome(start , end):
            while start <= end:
                if s[start] != s[end]:
                    return False
                start += 1
                end -= 1
            return True
        
        def backtrack(i):
            if i == n :
                res.append(sol[:])
                return
            
            for j in range(i , n):
                if isPalindrome(i , j):
                    sol.append(s[i : j + 1])
                    backtrack(j + 1)
                    sol.pop()
        
        backtrack(0)
        return res