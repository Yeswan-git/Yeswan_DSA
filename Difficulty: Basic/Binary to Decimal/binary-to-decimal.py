class Solution:
	def binaryToDecimal(self, b):
	    b = int(b)
	    res = 0
        exp = 0
		while b :
		    digit = b % 10
		    res += digit * 2 ** exp
		    exp += 1
		    b //= 10
	    return res