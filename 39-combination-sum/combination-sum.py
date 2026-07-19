class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        final=[]
        def fun(i,total,array):
            if total==target:
                final.append(array[:])
                return

            if i>=len(candidates) or total>target:
                return

            array.append(candidates[i])
            fun(i,total+candidates[i],array)

            array.pop()
            fun(i+1,total,array)

        fun(0,0,[])
        return final


            

        