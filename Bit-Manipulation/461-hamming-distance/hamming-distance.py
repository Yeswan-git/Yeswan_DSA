class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        count = 0
        XOR = x ^ y
        while XOR :
            count += XOR & 1
            XOR >>= 1
        return count