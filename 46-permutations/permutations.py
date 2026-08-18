class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        final=[]
        def back(out,target):
            if len(out)==target:
                final.append(out.copy())
            for x in nums:
                if x in out:
                    continue
                out.append(x)
                back(out,target)
                out.pop()

        back([],len(nums))
        return final



            
        