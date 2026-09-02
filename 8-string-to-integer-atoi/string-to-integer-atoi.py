class Solution:
    def myAtoi(self, s: str) -> int:
        if not s : return 0
        i = 0

        while i < len(s) and s[i] == " ":
            i += 1
        if not s or i == len(s) : return 0
        sign = 1
        if s[i] == "-":
            sign = -1
            i += 1
        elif s[i] == "+":
            i += 1
        

        INT_MAX = 2 ** 31 - 1
        INT_MIN = -2 ** 31
        res = 0
        while i < len(s) and s[i].isdigit():
            digit = int(s[i])
            nxt = res * 10 + digit
            if nxt > INT_MAX :
                return INT_MAX if sign == 1 else INT_MIN
            
            res = nxt
            i += 1
        
        return res * sign