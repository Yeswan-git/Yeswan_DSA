class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        k = len(needle)
        n = len(haystack)

        for i in range(n):
            if haystack[i : i + k] == needle :
                return i
        
        return -1