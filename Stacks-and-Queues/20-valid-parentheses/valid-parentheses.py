class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {")" : "(" , "}" : "{" , "]" : "["}
        stk = []

        for c in s :
            if c not in pairs :
                stk.append(c)
            else:
                if not stk :
                    return False
                else:
                    poped = stk.pop()
                    if poped != pairs[c] :
                        return False
        return not stk