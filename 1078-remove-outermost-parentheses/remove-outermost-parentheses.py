class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        balance = 0
        res = ""

        for c in s:
            if c == "(":
                if balance > 0:
                    res += c
                balance += 1
            else:
                balance -= 1
                if balance > 0:
                    res += c
        
        return res