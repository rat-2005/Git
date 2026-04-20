class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo={}

        def fun(value,n):
            
            if n==len(nums):
                if(value==target):
                    return 1
                else:
                    return 0

            if(value,n) in memo:
                return memo[(value,n)]
        
            out=fun(value+nums[n],n+1)+fun(value-nums[n],n+1)
            memo[(value,n)]=out

            return out
            
            

        return fun(0,0)
                

        