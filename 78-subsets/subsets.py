class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result=[]
        def backtrack(i,path):
            result.append(path.copy())
            for x in range(i,len(nums)):
                path.append(nums[x])
                backtrack(x+1,path)
                path.pop()
        backtrack(0,[])
        result.sort(key=len)
        return result


        