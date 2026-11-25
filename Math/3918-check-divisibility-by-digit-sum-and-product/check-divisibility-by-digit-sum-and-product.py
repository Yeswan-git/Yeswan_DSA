class Solution:
    def checkDivisibility(self, n: int) -> bool:
        copy = n
        digit_sum = 0
        digit_prd = 1
        while n :
            digit = n % 10
            digit_sum += digit
            digit_prd *= digit
            n //= 10
        return True if copy % (digit_sum + digit_prd) == 0 else False