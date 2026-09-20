class Solution:
    def reverseDegree(self, s: str) -> int:
        summ = 0
        for i in range(len(s)):
            summ += (26 - (ord(s[i]) - 97)) * (i + 1)
        return summ