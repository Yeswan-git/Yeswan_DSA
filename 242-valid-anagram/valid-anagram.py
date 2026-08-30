class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # return sorted(s) == sorted(t)
        from collections import Counter
        return Counter(s) == Counter(t)