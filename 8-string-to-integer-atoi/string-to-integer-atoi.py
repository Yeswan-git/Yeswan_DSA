class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        if not s : return 0
        i = 0
        sign = 1
        if s[i] == "+" :
            i += 1
        elif s[i] == "-" :
            sign = -1
            i +=1
        
        res = 0
        INT_MAX = 2 ** 31 - 1
        INT_MIN = -2** 31

        while i < len(s) and s[i].isdigit():
            digit = int(s[i])
            next_val = res * 10 + digit
            if next_val > INT_MAX :
                return INT_MAX if sign == 1 else INT_MIN
            
            res = next_val
            i += 1
        return res * sign