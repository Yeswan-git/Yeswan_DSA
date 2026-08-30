class Solution:
    def reverseWords(self, s: str) -> str:
        words = list(s.split())
        return " ".join(words[::-1])