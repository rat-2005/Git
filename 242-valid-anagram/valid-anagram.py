class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        else:
            freq=[0]*26
            for x in range(0,len(s)):
                freq[ord(s[x])-ord('a')]+=1
                freq[ord(t[x])-ord('a')]-=1
            for x in freq:
                if x!=0:
                    return False
        return True
        