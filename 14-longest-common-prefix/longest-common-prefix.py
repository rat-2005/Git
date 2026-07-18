class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        #sort it
        strs.sort()
        final=""
        for i in range(min(len(strs[0]),len(strs[-1]))):
            if strs[0][0:i+1]==strs[-1][0:i+1]:
                final=strs[0][0:i+1]
            else:
                break
        return final

 