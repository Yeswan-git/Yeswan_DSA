class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        count = 0
        XOR = start ^ goal
        while XOR:
            count += XOR & 1
            XOR >>= 1
        return count