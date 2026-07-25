class Solution:
    
    def countSubstrings(self, s: str) -> int:
        j=0
        for x in range(0,len(s)):
            for y in range(x,len(s)):
                if s[x:y+1]==s[x:y+1][::-1]:
                    j=j+1
        return j

        