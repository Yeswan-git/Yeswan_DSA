class Solution:
    def partition(self, s: str) -> list[list[str]]:
        n = len(s)
        res , sol = [] , []

        @cache
        def isPalindrome(start , end):
            if start >= end: return True
            return s[start] == s[end] and isPalindrome(start + 1 , end - 1)
        
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