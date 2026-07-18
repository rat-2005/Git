class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        #finding the length of the smallest
        l=9999
        for x in range(0,len(strs)):
            if len(strs[x])<l:
                l=len(strs[x])

        start=0
        dup=0
        com=strs[0]
        if len(strs)==1:
            return strs[0]
        final=""
        flag=False
        while(dup<l):
            for x in strs[1:]:
                if x[0:dup+1]==com[0:dup+1]:
                    flag=True
                else:
                    flag=False
                    break
            if flag==True:
                final=com[0:dup+1]

            dup=dup+1   
        return final     


        