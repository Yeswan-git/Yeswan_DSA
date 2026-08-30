class Solution:
    def largestOddNumber(self, num: str) -> str:
        n = len(num)
        if int(num[-1]) & 1 : return num
        for i in range(n - 2 , -1 , -1):
            if int(num[i]) & 1 :
                return num[:i + 1]
        return ""