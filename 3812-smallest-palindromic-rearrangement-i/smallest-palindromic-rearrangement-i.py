class Solution:
    def smallestPalindrome(self, s: str) -> str:
        n = len(s)
        if n == 1 : return s
        left = "".join(sorted(s[:n//2]))
        if n & 1:
            mid = s[n//2]
            return left + mid + left[::-1]
        else:
            return left + left[::-1]