class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        minn = float("inf")
        for s in strs :
            minn = min(minn , len(s))
        
        i = 0
        while i < minn :
            for s in strs :
                if s[i] != strs[0][i]:
                    return s[:i]
            i += 1
        
        return s[:i]