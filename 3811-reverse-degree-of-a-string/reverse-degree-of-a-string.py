class Solution:
    def reverseDegree(self, s: str) -> int:
        return sum((26 - (ord(s[i]) - 97)) * (i + 1) for i in range(len(s)))
        