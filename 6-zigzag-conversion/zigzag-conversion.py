class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows==1:
            return s
        m=[["_" for x in range(0,len(s))] for y in range(0,len(s))]
        r=0
        c=0
        index=0
        while(index<len(s)):
            while(r<numRows and index < len(s)):
                m[r][c]=s[index]
                r=r+1
                index=index+1
            c=c+1
            r=r-2
            for _ in range(0,numRows-2):
                if index >= len(s):
                    break
                m[r][c]=s[index]
                c=c+1
                r=r-1
                index=index+1
        out=""
        for x in m:
            for y in x:
                if y!="_":
                    out=out+y
        return out
    




        