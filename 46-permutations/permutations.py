class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        final=[]
        def recur(filled):
            if len(filled)==len(nums):
                final.append(filled[:])
            for x in nums:
                if x not in filled:
                    filled.append(x)
                    recur(filled)
                    filled.pop()

        recur([])
        return final

            
        