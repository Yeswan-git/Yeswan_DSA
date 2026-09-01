class Solution:
    def maxDepth(self, s: str) -> int:
        count = 0
        maxx = 0
        for c in s :
            if c == "(":
                count += 1
            elif c == ")":
                count -= 1
            maxx = max(maxx , count)
        return maxx