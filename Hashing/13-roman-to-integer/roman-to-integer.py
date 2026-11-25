class Solution:
    def romanToInt(self, s: str) -> int:
        roman_map = {"M" : 1000 , "D" : 500 , "C" : 100 , "L" : 50 , "X" : 10 , "V" : 5 , "I" : 1}
        ans = 0
        i = 0
        n = len(s)


        while i < n :
            if i + 1 < n and roman_map[s[i]] < roman_map[s[i + 1]] :
                ans += roman_map[s[i + 1]] - roman_map[s[i]]
                i += 2
            else:
                ans += roman_map[s[i]]
                i += 1
        
        return ans