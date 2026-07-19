class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        final=[]
        candidates.sort()

        def dfs(i,total,array):
            if total==target:
                if list(array[:]) not in final:
                    final.append(list(array[:]))
                return
            
            if target<total or len(candidates)<=i:
                return
            
            array.append(candidates[i])
            dfs(i+1,total+candidates[i],array)

            array.pop()
            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1
            dfs(i+1,total,array)

        dfs(0,0,[])
        return final