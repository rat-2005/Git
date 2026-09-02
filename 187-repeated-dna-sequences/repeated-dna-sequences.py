class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        l=[]
        hash={}
        for x in range(0,len(s)-10+1):
            if s[x:x+10] not in hash:
                hash[s[x:x+10]]=1
            elif s[x:x+10] not in l:
                l.append(s[x:x+10])
        return l
        